# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 08:54:32 2019

@author: santhob
"""

import cv2
import numpy as np



def _detectblue_color():
    cap = cv2.VideoCapture(0)
    while(1):
        
        _, frame = cap.read()
           # Convert BGR to HSV
       
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

