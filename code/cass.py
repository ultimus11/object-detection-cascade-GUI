import numpy as np
import cv2
handgest=cv2.CascadeClassifier("cascade.xml")

img = cv2.imread("13.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

hands = handgest.detectMultiScale(gray,1.01,5)
for (x,y,w,h) in hands:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	print("detected")
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()