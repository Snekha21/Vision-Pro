import cv2
import numpy as np
import face_recognition
from pytube import YouTube
import os

# Function to load the input image
def load_input_image(image_path):
    input_image = cv2.imread(image_path)
    return input_image

# Function to download and save the YouTube video
# Function to download and save the YouTube video
def download_youtube_video(video_url):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if video:
            video.download(filename='temp_video', output_path='.')
            video_path = 'temp_video.mp4'
            print("Video downloaded successfully:", video_path)
            return video_path
        else:
            print("Error: Unable to retrieve video stream.")
            return None
    except Exception as e:
        print("Error:", e)
        return None



import cv2

def recognizes_faces_in_video(video_url, input_image_path):
    # Load the input image
    input_image = cv2.imread(input_image_path)
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detection cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Process the video frames
    video_path = download_youtube_video(video_url)
    video_capture = cv2.VideoCapture('ts.mp4')

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Crop the face from the frame
            face_frame = frame[y:y+h, x:x+w]

            # Resize the input image to match the size of the detected face
            input_resized = cv2.resize(input_image, (w, h))

            # Compare the resized input image with the detected face
            difference = cv2.absdiff(face_frame, input_resized)

            # Convert the difference image to grayscale
            difference_gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

            # Compute the mean squared error (MSE) between the two images
            mse = (difference_gray ** 2).mean()

            # If the MSE is below a certain threshold, consider it a match
            if mse < 250:  # Adjust this threshold as needed
                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    video_capture.release()
    cv2.destroyAllWindows()

# Call the function with the provided inputs








if __name__ == "__main__":
    # Provide the YouTube video URL
    video_url = "https://youtu.be/cpainhYpvMQ?si=z-76qiSRVxwnFM4K"
    # Provide the path to the input image
    input_image_path = "ts.png"
    
    # Perform face recognition in the video
    recognizes_faces_in_video(video_url, input_image_path)
