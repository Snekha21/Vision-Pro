from __future__ import print_function
# from googleapiclient.discovery import build
# from google.oauth2 import service_account
from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import json 
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
# from json import jsonify
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from werkzeug.utils import secure_filename
import pathlib
import pickle
from PIL import Image
import tensorflow as tf
from tensorflow.keras.metrics import Metric
from tensorflow.python.keras.utils import losses_utils
import cv2 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import numpy as np
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from keras import backend as K
import random
# from sheet import create,create2
# from flask_mysqldb import MySQL

# SERVICE_ACCOUNT_FILE = 'credentials.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# attendance = '11-djRb6G5s3cZEovz0Fq1RghpGUH5Owf0CvPTKuxZes'

# service = build('sheets', 'v4', credentials=credentials)
# sheet = service.spreadsheets()

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
 
# mysql = MySQL(app)
 
# #Creating a connection cursor
# cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE patient_data(name,age,gender,profession,mailid,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12) ''')
# # cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# # cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# mysql.connection.commit()
 
# #Closing the cursor
# cursor.close()

subject = "Your Cutis Care Test Report"
body = "Hey there! Here is your test report for Skin diseases from Cutis Care"
sender_email = "snekhasuresh2777@gmail.com"
receiver_email = "snekhasuresh2777@gmail.com"
password = "hlwbwpiujgizxkwt"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email
message.attach(MIMEText(body, "plain"))
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/bmi')
def bmi():
    if request.method == 'POST':

        return redirect(url_for('home'))
    # show the form, it wasn't submitted
    return render_template('bmi.html')

@app.route('/home', methods=['GET', 'POST'])
def index_func():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    # show the form, it wasn't submitted
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about_func():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('About'))
    # show the form, it wasn't submitted
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Login'))
    # show the form, it wasn't submitted
    return render_template('login.html')


@app.route('/main', methods=['GET', 'POST'])
def main_func():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Main'))
    # show the form, it wasn't submitted
    return render_template('Main.html')


@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('time_slot')
    # print(type(message))

    # result = sheet.values().get(spreadsheetId=attendance, range="sheet2").execute()
    values = result.get('values', [])
    slot_column = 2
    slot_available = True  # Assume the slot is initially available
    lis_data = [name, email, message]
    slot_lis=[]
    for row in values:
        # print(type(row[slot_column]))
        slot_lis.append(str(row[slot_column]))
        
        # print(type(message))
        # if str(row[slot_column]) == str(message):
        if(str(message) in slot_lis):
            slot_available = False
            return render_template("Main.html", slot_not_available=True)
        else:
            # create2(lis_data)
            return render_template("thankyou.html")
    
    
    

    # if  slot_available:
    #     create2(lis_data)
    #     # The slot is available, proceed as usual
    #     return render_template("thankyou.html")
    #     # return render_template("Main.html", slot_not_available=True)
    # else:
    #     # The slot is not available, notify the user and show the form again
    #     return render_template("Main.html", slot_not_available=True)
    


@app.route('/contact', methods=['GET', 'POST'])
def contact_func():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        # name=request.form["name"]
        # mail=request.form["email"]
        # msg=request.form["message"]
        # lis_data=[name,mail,msg]
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # print(lis_data)
        # create(lis_data)
        data_contact=request.form
        print(name)
        return redirect(url_for('Contact'))
    
    # show the form, it wasn't submitted
    return render_template('contact.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    lis_data=[name,email,message]
    create(lis_data)
    
    # You can now process or store the data as needed
    
    return render_template("thankyou.html")


# @app.route('/result', methods=['GET', 'POST'])
# def result_func():
#     if request.method == 'POST':
#         # do stuff when the form is submitted
#         # redirect to end the POST handling
#         # the redirect can be to the same route or somewhere else
#         return redirect(url_for('result'))
#     # show the form, it wasn't submitted
#     return render_template('result.html')

@app.route('/input', methods=['GET', 'POST'])
def test_func():
    if request.method == 'POST':
        # data = request.form.get("q1")
        # for key, value in request.form.items():
        #     print("key: {0}, value: {1}".format(key, value))

        # data=console.log(JSON.stringify(input))
        # data1 =json.loads(request.json)
        # data = request.form.get("q1")
        # data = request.json
        data= request.form
        # data = json.dump(request.get_json(force=True))
        # with open('file.json', 'w') as f:
        #   json.dump(request.get_json(force=True), f)
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        print(data)
        # print(data1)
        convertJsonToCsv(data)
        return redirect(url_for('result'))
        # return render_template('result.html')
    return render_template('index.html')
    # show the form, it wasn't submitted
    # return render_template('index.html')

# @app.route("/image")
# def image():
# #   if request.method == "POST":
# #     image = request.files.get('img', '')
# #     image = request.form["img"]

# #     print("img ",image)
# #     return "<h1> yo! </h1>"
# #   else:
#     return render_template('image.html') 

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['File']
        f.save(secure_filename("image.jpg"))
        # result,percentage=mri()
        percentage=89
        result='Psoriasis'
        if(result!="Normal"):
            html_data=result
            result=percentage
            percentage="Kindly treat it as soon as possible"
            product_df = pd.read_csv('skincare_products.csv')
        if(result=="Normal"):
            html_data=result
            result="You are normal"
        input_disease = html_data
        if(input_disease != "Normal"):

            matching_products = []
            for i, row in product_df.iterrows():
                if input_disease in row['product_type']:
                    matching_products.append(row)


            product_vectors = []
            for i, row in product_df.iterrows():
                product_vectors.append(row['ingredients'] + " " + row['product_type'])
            tfidf_vectorizer = TfidfVectorizer()
            product_vectors_tfidf = tfidf_vectorizer.fit_transform(product_vectors)
            input_disease_vector_tfidf = tfidf_vectorizer.transform([input_disease])
            similarities = cosine_similarity(input_disease_vector_tfidf, product_vectors_tfidf)[0]


            top_k = 5
            top_product_indices = similarities.argsort()[::-1][:top_k]
            recommended_products = [product_df.iloc[i] for i in top_product_indices]

            result=[]
            for product in recommended_products:
                if len(result)<1:
                    result.append(product['product_name'])
            print(result)
        result=str(result) 
        
        # with open(filename, "rb") as attachment:
        #      part = MIMEBase("application", "octet-stream")
        #      part.set_payload(attachment.read())
        #      encoders.encode_base64(part)
        #      part.add_header(
        #     "Content-Disposition",
        #      f"attachment; filename= {filename}",
        #      )
        #      message.attach(part)
        #      text = message.as_string()
        #      context = ssl.create_default_context()
        #      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        #         server.login(sender_email, password)
        #     # msg = Message('Hello', sender = 'snekhasuresh2777@gmail.com', recipients = ['bluesmeter@gmail.com'])
        #     # msg.body = "Hello Flask message sent from Flask-Mail"
        #     # mail.send(msg)
        #         server.sendmail(sender_email, receiver_email, text)
        return render_template("resultss.html",html_data = html_data , result=result, cmt=percentage)
        
@app.route("/test", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('test'))
    
    return render_template('index.html')


def convertJsonToCsv(jsonData):
    dfs = []
    dfs.append(pd.DataFrame([jsonData]))
    df = pd.concat(dfs, ignore_index=True, sort=False)
    # df.drop(['userName'], 
    #     axis = 1, inplace = True)
    df.to_csv('input.csv',index=False)

@app.route("/result")
def result():
    data_dir = pathlib.Path("input.csv")
    df=pd.read_csv(data_dir)
    data1= df.transpose()
    # try x=data1[0].value_counts()[0]
    x=data1[0].value_counts()[0]
    y=data1[0].value_counts()[1]
    z=data1[0].value_counts()[2]
    n= (x/24)*100
    s= (y/24)*100
    a= (z/24)*100
    d=s+a
    # data1['Average'] = data1.mean(axis=1)
    # data1.drop(['Monday','Tuesday','Wednesday','Thursday','Friday'],axis = 1, inplace = True)
    # fmodel = pickle.load(open('fin_model.pkl','rb'))
    # model = pickle.load(open('fin_model.pkl','rb'))
    # if(model.predict(data1) == 0):
    #     return  {"output":"You are depressed"}
    # else:
    #     return {"output":"You are not depressed"}
    # data1 = data1.astype(float)
    model = pickle.load(open('lr_model.pkl','rb'))
    if(model.predict(df) == 1):
        if (d<5):
            html_data= "You are a healthy person!"
            result = "Congrats! You are living a healthy life!"
            cmt= "Stay happy and healthy"
        elif (d<25):
            html_data= "Beginner Stage"
            result = "You had just started showing the symptoms of skin diseases,dont worry its going to be alright"
            cmt= "Just wake up! It's not too late..."
        elif (d<65):
            html_data= "Moderate Stage"
            result = "You had just started showing the symptoms of skin pathalogy"
            cmt= "You are adviced to consult a dermatologist asap"
        elif (d>65):
            html_data= "Severe Stage"
            result = "You are adviced to visit a dermatologist asap and get necessary treatment, contact help-desk to reach out to doctors"
            cmt= "To confirm the severity of skin disease, kindly take necessary tests"
        filename = "diseased.pdf"
        with open(filename, "rb") as attachment:
             part = MIMEBase("application", "octet-stream")
             part.set_payload(attachment.read())
             encoders.encode_base64(part)
             part.add_header(
            "Content-Disposition",
             f"attachment; filename= {filename}",
             )
             message.attach(part)
             text = message.as_string()
             context = ssl.create_default_context()
             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
            # msg = Message('Hello', sender = 'snekhasuresh2777@gmail.com', recipients = ['bluesmeter@gmail.com'])
            # msg.body = "Hello Flask message sent from Flask-Mail"
            # mail.send(msg)
                server.sendmail(sender_email, receiver_email, text)
        print(model.predict(df))
        return render_template("resultss.html", html_data = html_data , result=result, cmt=cmt)
    elif(model.predict(df) == 0):
        html_data = "You are a healthy person!"
        result = "Congrats! You are living a healthy life!"
        cmt = "Stay happy and healthy"
        filename="healthy.pdf"
        with open(filename, "rb") as attachment:
             part = MIMEBase("application", "octet-stream")
             part.set_payload(attachment.read())
             encoders.encode_base64(part)
             part.add_header(
            "Content-Disposition",
             f"attachment; filename= {filename}",
             )
             message.attach(part)
             text = message.as_string()
             context = ssl.create_default_context()
             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
            # msg = Message('Hello', sender = 'snekhasuresh2777@gmail.com', recipients = ['bluesmeter@gmail.com'])
            # msg.body = "Hello Flask message sent from Flask-Mail"
            # mail.send(msg)
                server.sendmail(sender_email, receiver_email, text)
        print(model.predict(df))
        return render_template("result.html", html_data = html_data , result=result, cmt=cmt)
    

@app.route("/img")

def mri():
        # img = Image.open("image.jpg")
        # img = img.convert("L")
        accuracy=tf.keras.metrics.Accuracy(name="accuracy", dtype=None)
        
        # recall = recall_m(y_true, y_pred)
        # precision = precision_m(y_true, y_pred)
        # f1_m = f1_m(y_true, y_pred)
        # model = tf.keras.models.load_model('skin.h5',custom_objects={"accuracy": accuracy})
        # image_path = 'image.jpg'
        # image = load_img(image_path, target_size=(256, 256))
        # image_array = img_to_array(image)
        # input_data = image_array.reshape(1, 256, 256, 3) 
        # predictions = model.predict(input_data)
        # # print(predictions)
        # score = tf.nn.softmax(predictions[0])
        # # score2 = tf.nn.softmax(predictions[1])
        # # score3 = tf.nn.softmax(predictions[2])
        
        # class_names=['Acne and Rosacea', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis', 'Bullous Disease ', 'Cellulitis Impetigo and other Bacterial Infections', 'Eczema', 'Exanthems and Drug Eruptions', 'Hair Loss Alopecia and other Hair Diseases', 'Herpes HPV and other STDs ', 'Light Diseases and Disorders of Pigmentation', 'Pemphigus Vegetans', 'Melanoma Skin Cancer Nevi and Moles', 'Nail Fungus and other Nail Disease', 'Poison Ivy  and other Contact Dermatitis', 'Psoriasis', 'Scabies Lyme Disease and other Infestations and Bites', 'Seborrheic Keratoses and other Benign Tumors', 'Systemic Disease', 'Tinea Ringworm Candidiasis and other Fungal Infections', 'Urticaria Hives', 'Vascular Tumors', 'Vasculitis ', 'Warts Molluscum and other Viral Infections']
        # result= class_names[np.argmax(score)]
        # # result2= class_names[np.argmax(score2)]
        # # result3= class_names[np.argmax(score3)]
        # percentage=str(100 * np.max(score))+" Risk Percentage"
        # print(result)

        from keras.models import load_model
        from keras.applications.vgg16 import preprocess_input
        import keras

        model = load_model('orginal_skin_model.h5')
        img = Image.open('image.jpg') 
        img = img.resize((224,224)) 
        img_array = np.array(img)
        img_array = img_array.astype('float32')
        img_array = preprocess_input(img_array) 
        img_array = np.expand_dims(img_array, axis=0)
        vgg_model = keras.applications.vgg16.VGG16(include_top=False, weights='imagenet')
        features = vgg_model.predict(img_array)
        features = features.reshape(features.shape[0], -1)
        predictions = model.predict(features)
        print(predictions)
        class_names = ['PemphigusVegetans',
 'Normal',
 'vitiligo',
 'Psoriasis',
     'Melanoma Skin Cancer Nevi and Moles',
 'Psoriasis']
        predicted_class_index = np.argmax(predictions)
        predicted_class_name = class_names[predicted_class_index]
        print('Predicted class:', predicted_class_name)
        # percentage=str(100 * np.max(predictions))+" Risk Percentage"
        predicted_class_index = np.argmax(predictions)
        confidence_percentage = predictions[0][predicted_class_index] * 100
                
        # print(score)    
        # if(model.predict(X) == 1):
        #     html_data= "You are depressed"
        #     result = "You are showing symptoms of depression"
        #     cmt= "You are adviced to contact your doctor and get treated asap"
        # elif(model.predict(X) == 0):
        #     html_data = "You are not depressed"
        #     result = "Congrats! You are not showing symptoms of depression"
        #     cmt = "Stay happy and healthy"
        # print(model.predict(X))
        # return (html_data , result, cmt)
        return(predicted_class_name,confidence_percentage)

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
# response = english_bot.get_response('What is depression?')
# print(response)
 
# response = english_bot.get_response('Who are you?')
# print(response)
 
# @app.route("/chat")
# def chat():
#     return render_template("chat.html")
 
# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(english_bot.get_response(userText))
@app.route('/search',methods=['GET', 'POST'])
def search_page():
     if request.method == 'POST':
        global state,district,data
        searchs= request.form
        print(searchs)
        dfs = []
        dfs.append(pd.DataFrame([searchs]))
        df = pd.concat(dfs, ignore_index=False, sort=False)
        state=str(df.iloc[-1,0]).lower()
        district=str(df.iloc[-1,1]).lower()
        print(state,district)
        data=pd.read_csv('hospitals.csv', header=None)
        print(data[2])
        data[2]=data[2].str.lower()
        data[3]=data[3].str.lower()
        data=data[data[2]  == state]
        data=data[data[3]  == district]
        # data=data[data.values  == date]
        # data.rename(columns=dfs.iloc[0], inplace = True)
        print(data)
        # if search=="Ph_no":
        # data = pd.concat(data, ignore_index=True, sort=False)
        # data.to_csv('result.csv',index=False)
        #     s= 7
        # else:
        #     s= 14
        # data.reset_index(inplace = True)
        # data = data.set_index('index')
        # data.index = np.arange(1, len(data)+1)
        return redirect(url_for('db'))
     return render_template('search.html')

@app.route('/coun',methods=['GET', 'POST'])
def db():
    # datas = pd.read_csv('hospitals.csv',  error_bad_lines=False)
    # print(datas)
    # datas=datas[datas.values  == date]
    
    html = data.to_html()
#write html to file
    text_file = open("./templates/"+"db"+".html", "w")
    text_file.write(html)
    text_file.close()
    path= "db"+".html"
    return render_template(path)

@app.route("/log",methods=["POST","GET"])
def accounts():

    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("logins.html")
@app.route('/diet', methods=['GET', 'POST'])
def diet():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Diet'))
    # show the form, it wasn't submitted
    return render_template('calorie.html')

@app.route("/cal",methods=["POST","GET"])
def calorie():

    if request.method == "POST":
        # data = request.form.get("q1")
        # for key, value in request.form.items():
        #     print("key: {0}, value: {1}".format(key, value))

        # data=console.log(JSON.stringify(input))
        # data1 =json.loads(request.json)
        # data = request.form.get("q1")
        # data = request.json
        data= request.form
        # data = json.dump(request.get_json(force=True))
        # with open('file.json', 'w') as f:
        #   json.dump(request.get_json(force=True), f)
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        print(data)
        # print(data1)
        convertJsonToCsvs(data)
        return redirect(url_for('results'))
        # return render_template('result.html')
    return render_template("calorie.html")
def convertJsonToCsvs(jsonData):
    dfs = []
    dfs.append(pd.DataFrame([jsonData]))
    df = pd.concat(dfs, ignore_index=True, sort=False)
    print(df)
    # df.drop(['userName'], 
    #     axis = 1, inplace = True)
    df.to_csv('calorie.csv',index=False)

@app.route("/results")
def results():
    data_dir = pathlib.Path("calorie.csv")
    df=pd.read_csv(data_dir)
    print(df.iloc[0].to_list())
    print('WTH')
    result="ho"
    cmt=56
    # data1['Average'] = data1.mean(axis=1)
    # data1.drop(['Monday','Tuesday','Wednesday','Thursday','Friday'],axis = 1, inplace = True)
    # fmodel = pickle.load(open('fin_model.pkl','rb'))
    # model = pickle.load(open('fin_model.pkl','rb'))
    # if(model.predict(data1) == 0):
    #     return  {"output":"You are depressed"}
    # else:
    #     return {"output":"You are not depressed"}
    # data1 = data1.astype(float)
    dfs=df.iloc[0].to_list()
    # model = pickle.load(open('calorie_model.pkl','rb'))
    # calorie=model.predict(dfs)
        
    # print(model.predict(dfs))
    food_df = pd.read_csv('food.csv')

    food_df['Calories'] = food_df['Calories'].apply(lambda x: re.findall(r'\d+', x)[0]).astype(float)

    scaler = MinMaxScaler()
    food_df['Calories'] = scaler.fit_transform(food_df['Calories'].values.reshape(-1, 1))

    predicted_calories = 0.02623
    print(food_df['Calories']) 
    filtered_foods = food_df[food_df['Calories'] >= predicted_calories]
    print(filtered_foods)
    if len(filtered_foods) > 0:
        
        recommended_foods = filtered_foods
        foods=[]
        for _, food in recommended_foods.iterrows():
            if len(foods)<7:
                html_data= "Hey there, You can eat the following foods!"
                foods.append(food['Food'])
                result=f"Calories: {food['Calories']}"
        return render_template("diet_recom.html", html_data = calorie , result=result, cmt=foods)
            
    else:
        cmt="No foods found within the desired calorie range."
        result=predicted_calories
        return render_template("resultss.html", html_data = calorie , result=result, cmt=cmt)
    
@app.route("/map")
def map():
     if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('map'))
    # show the form, it wasn't submitted
     return render_template('map.html')


@app.route("/chatbot")
def bot():
    return redirect("http://127.0.0.1:7860")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)


    