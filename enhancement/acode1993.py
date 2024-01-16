import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# 绘制直方图函数
def grayHist(img):
    h, w = img.shape[:2]
    pixelSequence = img.reshape([h * w, ])
    numberBins = 256
    histogram, bins, patch = plt.hist(pixelSequence, numberBins,
                                      facecolor='black', histtype='bar')
    plt.xlabel("gray label")
    plt.ylabel("number of pixels")
    plt.axis([0, 255, 0, np.max(histogram)])
    plt.show()
name=("1993_10_12_B1.tif","1993_10_12_B2.tif","1993_10_12_B3.tif","1993_10_12_B4.tif","1993_10_12_B5.tif","1993_10_12_B6.tif","1993_10_12_B7.tif")
for i,j in enumerate(name):
    img = cv.imread(j, 0)
# 计算原图中出现的最小灰度级和最大灰度级
# 使用函数计算
    Imin, Imax = cv.minMaxLoc(img)[:2]
# 使用numpy计算
# Imax = np.max(img)
# Imin = np.min(img)
    Omin, Omax = 0, 255
# 计算a和b的值
    a = float(Omax - Omin) / (Imax - Imin)
    b = Omin - a * Imin
    out = a * img + b
    out = out.astype(np.uint8)
    cv.namedWindow('data_before', cv.WINDOW_FREERATIO)
    cv.imshow("data_before", img)
    grayHist(img)#
    cv.namedWindow('data_after', cv.WINDOW_FREERATIO)#自适应窗口
    cv.imshow("data_after", out)
    grayHist(out)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #cv.imwrite(str(i)+'.tif',out)
print('处理完毕')
