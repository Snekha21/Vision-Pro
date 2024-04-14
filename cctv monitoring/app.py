from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from pymongo import MongoClient
import urllib.parse
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch
import os
import cv2

app = Flask(__name__)



def extract_frames(video_path, output_folder):
    video_reader = cv2.VideoCapture(video_path)
    frame_count = 0
    while video_reader.isOpened():
        ret, frame = video_reader.read()
        if not ret:
            break
        frame_path = f"{output_folder}/frame_{frame_count}.jpg"
        cv2.imwrite(frame_path, frame)

        frame_count += 1
        print(frame_count)
    video_reader.release()
# input_video_path = "intro.mp4"
output_frames_folder = "output"
# extract_frames(input_video_path, output_frames_folder)

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
app.secret_key = 'abc'
folder_path = "output"
mongodb_uri = "mongodb+srv://harshan:" + urllib.parse.quote("Harshan@1803") + "@cluster0.ixfzmsm.mongodb.net/?retryWrites=true&w=majority"
database_name = 'credentials_db'
client = MongoClient(mongodb_uri)
db = client[database_name]
users_collection = db['users']

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_auth = request.form['nm']
        pwd_auth = request.form['pwd']
        user_data = users_collection.find_one({'email': user_auth})

        if user_data and str(user_data['password']) == pwd_auth:
            session['user'] = str(user_data['_id'])  
            return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html',user=session["user"])

@app.route('/frames', methods=['POST', 'GET'])
def frames():
    detections = []

    if request.method == 'POST':
        video_file = request.files['video']
        prompt = request.form['prompt']

        video_path = 'uploaded_video.mp4' 
        video_file.save(video_path)
        # extract_frames(video_path, output_frames_folder)

        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"): 
                image_path = os.path.join(folder_path, filename)
                image = Image.open(image_path)
                inputs = processor(images=image, return_tensors="pt")
                outputs = model(**inputs)

                target_sizes = torch.tensor([image.size[::-1]])
                results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

                for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
                    if score >= 0.5 and model.config.id2label[label.item()] == prompt:
                        box = [round(coord, 2) for coord in box.tolist()]
                        detection_info = f"Detected {model.config.id2label[label.item()]} with confidence " \
                                        f"{round(score.item(), 3)} at location {box}"
                        detections.append({"image_path": image_path, "info": detection_info})

    return render_template('frame.html', detections=detections)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
