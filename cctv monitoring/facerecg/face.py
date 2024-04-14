from gettext import install
import cv2
import numpy as np
import face_recognition

imgney = face_recognition.load_image_file("/home/kishore/facerecg/pics/neymar.jpg")
imgney = cv2.cvtColor(imgney,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file("/home/kishore/facerecg/neymartest.jpg")
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgney)[0]
encodeney = face_recognition.face_encodings(imgney)[0]
cv2.rectangle(imgney,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)


faceloctest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

result= face_recognition.compare_faces([encodeney],encodetest)
facedis = face_recognition.face_distance([encodeney],encodetest)
print(result,facedis)



cv2.imshow("neymar",imgney)
cv2.imshow("neymar test",imgtest)
cv2.waitKey(0)