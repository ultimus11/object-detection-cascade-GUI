import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
handgest=cv2.CascadeClassifier("cascade.xml")

img = cv2.imread("gr5.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


eye = eye_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in eye:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	print("detected")
face = face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in face:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	print("detected")

hands = handgest.detectMultiScale(gray,1.01,5)
for (x,y,w,h) in hands:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	print("detected")

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()