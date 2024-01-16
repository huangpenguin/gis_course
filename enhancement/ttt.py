import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('666.jpg')
b,g,r=cv2.split(img)
cv2.imshow('data1',b)
cv2.imshow('data2',g)
cv2.imshow('data3',r)
cv2.waitKey(0)