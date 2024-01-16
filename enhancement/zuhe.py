import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#文件名需要将完整的后缀附上
#opencv函数操作时分离的通道是按照BGR的顺序
data1 = cv.imread('2.tif', 0)
data2 = cv.imread('1.tif', 0)
data3 = cv.imread('0.tif', 0)
data = cv.merge([data3,data2,data1])
#data = np.array((data1, data2, data3),dtype = data1.dtype)
#print(data1.shape)
#print(data.shape)
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('321.tif',data)
cv.waitKey(0)

data1 = cv.imread('3.tif', 0)
data2 = cv.imread('2.tif', 0)
data3 = cv.imread('1.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('432.tif',data)
cv.waitKey(0)

data1 = cv.imread('3.tif', 0)
data2 = cv.imread('4.tif', 0)
data3 = cv.imread('0.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('451.tif',data)
cv.waitKey(0)

data1 = cv.imread('6.tif', 0)
data2 = cv.imread('3.tif', 0)
data3 = cv.imread('0.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('741.tif',data)
cv.waitKey(0)

data1 = cv.imread('9.tif', 0)
data2 = cv.imread('8.tif', 0)
data3 = cv.imread('7.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('321-2005.tif',data)
cv.waitKey(0)

data1 = cv.imread('10.tif', 0)
data2 = cv.imread('9.tif', 0)
data3 = cv.imread('8.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('432_2005.tif',data)
cv.waitKey(0)

data1 = cv.imread('10.tif', 0)
data2 = cv.imread('11.tif', 0)
data3 = cv.imread('7.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('451_2005.tif',data)
cv.waitKey(0)

data1 = cv.imread('13.tif', 0)
data2 = cv.imread('10.tif', 0)
data3 = cv.imread('7.tif', 0)
data = cv.merge([data3,data2,data1])
cv.namedWindow('data', cv.WINDOW_FREERATIO)
cv.imshow('data',data)
cv.imwrite('741_2005.tif',data)
cv.waitKey(0)




'''img = cv2.imread("mini.jpg")
b, g, r = cv2.split(img)
cv2.imshow("Blue", r)
cv2.imshow("Red", g)
cv2.imshow("Green", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 也可以单独返回其中一个通道  
b = cv2.split(img)[0]  # B通道  
g = cv2.split(img)[1]  # G通道  
r = cv2.split(img)[2]  # R通道  '''#图像通道分离