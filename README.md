Prototype Overview: Vision Pro

Vision Pro is an advanced police assistance platform designed to empower law enforcement agencies with cutting-edge technology for crime detection, traffic management, and community safety. This prototype integrates AI, IoT hardware, and innovative analytics to enhance operational efficiency and proactive crime prevention.

The project is divided into four phases


## 1)Foresight - An all in one Dashboard for Police Department
Features 
Real-time Anomaly Detection
Incident Prediction
Automated Alerts
Easy Integration
User-Friendly Interface

## 2)Streamlit-Prophet : All in one Live Data training and analytics tool for resource allocations
Now you can train, evaluate and optimize forecasting models in a few clicks. All you have to do is to upload a time series dataset.
-Prepare data: Filter, aggregate, resample and/or clean your dataset.
-Choose model parameters: Default parameters are available but you can tune them. Look at the tooltips to understand how each parameter is impacting forecasts.
-Select evaluation method: Define the evaluation process, the metrics and the granularity to assess your model performance.
-Make a forecast: Make a forecast on future dates that are not included in your dataset, with the model previously trained.
-Once you are satisfied, click on "save experiment" to download all plots and data locally.

![Github Link to StreamlitProphet](https://github.com/Snekha21/Prophet_Ksp)
![Link to StreamlitProphet app](https://prophetksp.streamlit.app/)

## 3)VisionBot - A trained ChatBot for Police emergency services
![Link to Chatbot](https://chatbotksp.streamlit.app/)

Features of this chatbot

-Emergency Reporting
-Information Retrieval
-Integration with Emergency Services
-Status Updates
-Mental Health and Counseling Support

## 4) A cyber security based dashboard
![Link to Dashboard](https://public.datapine.com/?_ga=2.237124416.1337044665.1716047872-1012320311.1716047872#board/DhRDmjO5zXeJni2rP7iBIT)
# Foresight - Dashboard 🚀

<div align="center">

_A modern CCTV management system with hazard detection for efficient incident response 🛡️._


_Foresight: Real-time CCTV 📹 Fire and Weapon detection and incident prediction. YOLOV8-powered 🧠 security for proactive threat prevention._
</div>




## Introduction 🌟
_Project Foresight_ is an YOLOV8-powered security system 🛡️ designed to provide proactive threat prevention by analyzing real-time CCTV footage. Our system identifies potential hazards and anomalies, ensuring timely and efficient incident response.

## Features 🚀
- **Real-time Anomaly Detection:** Utilizes cutting-edge AI to monitor CCTV footage for unusual activity.
- **Incident Prediction:** Predicts potential incidents before they occur, enhancing proactive measures.
- **Automated Alerts:** Notifies relevant authorities and individuals upon detection of any threats.
- **Easy Integration:** Seamlessly integrates with existing CCTV infrastructure.
- **User-Friendly Interface:** Intuitive design for ease of use and efficient management.

## Tech-stack 💻
Our system is built using the latest technologies for optimal performance and scalability.

![page github 2](https://github.com/oceands/Project_Foresight/assets/94485584/c04d9c56-9242-4223-8c19-674ec8026358)

## Installation Guide 🛠️

### Frontend Setup
Clone the Repository

Enter Client Dir
```sh
cd client
```
Install packages
```sh
npm install --force
```
Run Front End Server 
```sh
npm run start
```


### Backend Setup
Change to Server Directory
```sh
cd server
```
Create a Venv
```sh
python3 -m  venv .venv
```
Activate venv
```sh
.venv/Scripts/Activate
```
Install Requirments
```sh
pip install - r requirements.txt
```
Run Flask Server
```sh
flask run
```
### WebRTC server Setup
Change to Server Directory
```sh
cd RTSPtoWeb
```
Run server
```sh
go run .
```

### Additional Setup

#### Postman API Setup
Configure and Use Postman for API Testing
- Install Postman on your device.
- Open Postman and either sign up or log in.
- Enter the following URL in a new tab: `http://127.0.0.1:5000/auth/api/users/register`
- Set the method to POST and body to raw JSON.
- Enter user details as shown in the example:

  ```json
  {
      "Fname": "First Name",
      "Lname": "Last Name",
      "email": "email@example.com",
      "role": "user role",
      "password": "your password"
  }
  ```

- Send the request in Postman.
- Log in on the frontend using the provided email and password







