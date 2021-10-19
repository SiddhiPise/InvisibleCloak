import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

time.sleep(2) 
bgimg = 0

for i in range(60): 
    ret, bgimg = cam.read()

m
ca


while (cam.isOpened()):
    ret, current_frame = cam.read()

    if ret:
        hsv_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #lower range color
        l_blue = np.array([110, 120, 170])
        u_blue = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv_img, l_blue, u_blue)

        #upper range color
        l_blue = np.array([180, 120, 170])
        u_blue = np.array([240, 255, 255])
        mask2 = cv2.inRange(hsv_img, l_blue, u_blue)

        full_mask = mask1+mask2

        part1 = cv2.bitwise_and(bgimg, bgimg, mask=full_mask)

        part2 = cv2.bitwise_not(full_mask)

        full_part = cv2.bitwise_and(current_frame, current_frame, mask = part2)

        cv2.imshow('wow', part1 + full_part)


cam.release()
cv2.destroyAllWindows()