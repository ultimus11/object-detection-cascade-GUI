import cv2
import os
import sys

cap = cv2.VideoCapture(0)

start = False
number_of_imgs = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if number_of_imgs == 200:
        break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        roi = frame[100:500, 100:500]
        save_path = "images_t/test1/"+'{}.jpg'.format(number_of_imgs)
        cv2.imwrite(save_path, roi)
        number_of_imgs += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(number_of_imgs),
            (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('s'):
        start = True

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
