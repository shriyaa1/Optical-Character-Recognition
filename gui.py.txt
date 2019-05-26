# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:02:21 2019

@author: shriya
"""

import cv2
import pytesseract
def detect(gray, frame):
    
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    
    cv2.imwrite("C:\\Users\\shriya\\Desktop\\Machine Learning A-Z\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\p.png", frame)
    text=pytesseract.image_to_string("C:\\Users\\shriya\\Desktop\\Machine Learning A-Z\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\p.png")
    print(text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()




































