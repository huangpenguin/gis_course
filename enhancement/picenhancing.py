import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


'''def calcGrayHist(I):
    # 计算灰度直方图
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist

img = cv.imread("6666.TIF", 0)
grayHist = calcGrayHist(img)
x = np.arange(256)

# 绘制灰度直方图
plt.plot(x, grayHist, 'r', linewidth=2, c='black')
plt.xlabel("gray Label")
plt.ylabel("number of pixels")
plt.show()




#合并通道img=cv2.merge(b,g,r)'''
#img为[行，列，通道数]
import cv2

img = cv2.imread('1993_10_12_B2.tif')
#cv2.imshow('img', img)
rows, cols, channels = img.shape
dst = img.copy()
#print(img.shape)
a = (255-0)/(np.max(img)-np.min(img))
b = -a*np.min(img)+0
for i in range(rows):
    for j in range(cols):
        for c in range(3):
            color = img[i, j][c] * a + b
            if color > 255:
                dst[i, j][c] = 255
            elif color < 0:
                dst[i, j][c] = 0
print(dst)
'''cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()'''


