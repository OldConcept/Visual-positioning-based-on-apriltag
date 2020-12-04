'''
Author: OldConcept
Date: 2020-12-05 01:34:56
LastEditors: OldConcept
LastEditTime: 2020-12-05 03:10:10
FilePath: \py\rm_server\t1.py
'''
import cv2 as cv
import apriltag

cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
at_detector =  apriltag.Detector(apriltag.DetectorOptions(families='tag36h11'))


def detect():
    while cap.isOpened():
        key = cv.waitKey(45)
        if key & 0x00FF == 27:
            break
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        tags = at_detector.detect(gray)
        for tag in tags:
            cv.circle(frame, tuple(tag.corners[0].astype(int)), 4,(0,0,255), 2) # left-top
            cv.circle(frame, tuple(tag.corners[1].astype(int)), 4,(0,0,255), 2) # right-top
            cv.circle(frame, tuple(tag.corners[2].astype(int)), 4,(0,0,255), 2) # right-bottom
            cv.circle(frame, tuple(tag.corners[3].astype(int)), 4,(0,0,255), 2) # left-bottom
            cv.circle(frame, tuple(tag.center.astype(int)), 4,(0,0,255), 2) #center
        cv.imshow('image', frame)
    cap.release()
    cv.destroyAllWindows()