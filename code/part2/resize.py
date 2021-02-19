import cv2
import numpy as np
IMG_SIZE=200
#img_array = cv2.imread("gr.jpg" ,cv2.IMREAD_GRAYSCALE)
img_array = cv2.imread("gr.jpg")
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
cv2.imwrite("gr2.png",new_array)