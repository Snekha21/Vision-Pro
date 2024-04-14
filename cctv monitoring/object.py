import cv2
from roboflow import Roboflow

# Initialize Roboflow for model inference
rf = Roboflow(api_key="1XpjtVozI07Y2KQN12Mw")
project = rf.workspace().project("violence-weapon-detection")
model = project.version(1).model

# Read video from URL or file (replace 'YOUR_VIDEO_URL' with the actual URL)
video_url = "NV_1.mp4"
cap = cv2.VideoCapture(video_url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Perform inference on the frame
    result = model.predict(frame, confidence=0.5, overlap=0.3).json()
    predictions = result["predictions"]

    # Visualize predictions on the frame (add bounding boxes, labels, etc.)
    # Draw bounding boxes on 'frame' using 'predictions'

    # Display the frame with predictions
    cv2.imshow("Video with Predictions", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
