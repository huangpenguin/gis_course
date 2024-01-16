import cv2
import numpy as np
import matplotlib.pyplot as plt


spot = cv2.imread('spot.tif')
multi = cv2.imread('743.tif',0)
cv2.namedWindow('data', cv2.WINDOW_NORMAL)
cv2.imshow('data',multi)
cv2.waitKey(0)
img=multi


#Y_prediction_test = np.squeeze(d['Y_prediction_test'])

'''rows, cols = sky.shape[:2] #获取sky的高度、宽度
#print(sky.shape[:2]) #(800, 1200)
#print(bear.shape[:2]) #(224, 224)
bear_dst = cv2.resize(bear,(cols,rows),interpolation=cv2.INTER_CUBIC) #放大图像'''#分辨率不一样处理模块
#add_img = cv2.addWeighted(spot,a,multi,b,c) #图像融合

print(img.shape)
#b3,g4,r7=cv2.split(multi)
b3 = cv2.split(img)[0]  # B通道
g4 = cv2.split(img)[1]  # G通道
r7 = cv2.split(img)[2]  # R通道  #图像通道分离


'''b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
b[:, :] = img[:, :, 0]
g[:, :] = img[:, :, 1]
r[:, :] = img[:, :, 2]'''


cv2.imshow('data1',b3)
cv2.imshow('data2',g4)
cv2.imshow('data3',r7)
#cv2.imshow('data',cv2.merge([r7,g4,b3]))
cv2.waitKey(0)

'''b3 = cv2.split(multi)[0]  # B通道
g4 = cv2.split(multi)[1]  # G通道
r7 = cv2.split(multi)[2]  # R通道  #图像通道分离


did1 = cv2.divide(b3,multi)
result1=cv2.multiply(did1,spot)
cv2.imwrite('bizhi1.tif',result1)
did2= cv2.divide(g4,multi)
result2=cv2.multiply(did2,spot)
cv2.imwrite('bizhi2.tif',result2)
did3 = cv2.divide(r7,multi)
result3=cv2.multiply(did3,spot)
cv2.imwrite('bizhi3.tif',result3)

multiresult=cv2.multiply(spot,multi)
cv2.imwrite('chengji1.tif',result3)
#help(cv2.addWeighted)可得到.addWeighted函数的官方解释。

'''
'''# 显示图片
titles = ['BearBrown','Sky','add_img']
imgs = [bear,sky,add_img]
for i in range(len(imgs)):
    plt.subplot(2,3,i+1)
    imgs[i]=cv2.cvtColor(imgs[i],cv2.COLOR_BGR2RGB)
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
'''
