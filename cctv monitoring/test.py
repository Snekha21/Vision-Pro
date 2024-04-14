import cv2
import winsound
from skimage.metrics import structural_similarity as compare_ssim


def difference(frame1, frame2):
    # convert the images to grayscale

    grayA = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    medianA = cv2.medianBlur(grayA ,5)
    grayB = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    medianB = cv2.medianBlur(grayB ,5)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(medianA, medianB, full=True)
    diff = (diff * 255).astype("uint8")
    # print("SSIM: {}".format(score))
    return score

x, y, width, height = cv2.selectROI(first_frame)
roi = first_frame[y: y + height, x: x + width]
video = cv2.VideoCapture('Test.mp4')
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
codec = cv2.VideoWriter_fourcc(*'XVID')
fps =int(video.get(cv2.CAP_PROP_FPS))
cap_width, cap_height = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter('test1.avi', codec, fps, (cap_width, cap_height), True)
_, first_frame = video.read()

while True:
    _, frame = video.read()
    if frame is None:
        break
    roi_new = frame[y: y + height, x: x + width]
    # avg1= np.mean(roi_new)
    # print(avg1)
    similarity = difference(roi, roi_new)
    if similarity < 0.8:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        winsound.Beep(500, 200)
    cv2.imshow('new_frame', frame)
    output.write(frame)
    cv2.waitKey(10)
output.release()
video.release()
cv2.destroyAllWindows()