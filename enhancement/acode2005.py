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
name=("2005_09_11_B1.tif","2005_09_11_B2.tif","2005_09_11_B3.tif","2005_09_11_B4.tif","2005_09_11_B5.tif","2005_09_11_B6.tif","2005_09_11_B7.tif")
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
    '''cv.imshow("img", img)
    grayHist(img)
    cv.imshow("out", out)
    grayHist(out)
    cv.waitKey(0)
    cv.destroyAllWindows()'''
    cv.imwrite(str(i+7)+'.tif',out)
print('处理完毕')
