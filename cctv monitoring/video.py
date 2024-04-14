import cv2

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
input_video_path = "uploaded_video.mp4"
output_frames_folder = "output"
extract_frames(input_video_path, output_frames_folder)
