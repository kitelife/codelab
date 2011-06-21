# -*- coding:utf-8 -*-
###########################################################
# OpenCV example
#
# cvLoadImage, cvSaveImage, cvCreateImage, cvCopy
# 以及图像显示的例子
#
# By ChaiShushan 2008
###########################################################
 
import sys
 
# 导入OpenCV模块
 
from opencv.cv import *
from opencv.highgui import *
 
if __name__ == '__main__':
 
    if len(sys.argv) == 3:
 
        # 载入图像，强制转化为Gray
 
        pImg = cvLoadImage(sys.argv[1], 0)
        if not pImg: sys.exit(-1)
 
        # 创建同样大小的图小
 
        pImg2 = cvCreateImage(cvGetSize(pImg), pImg.depth, pImg.nChannels)
 
        # 复制图像
 
        cvCopy(pImg, pImg2, None)
 
        # 把图像写入文件
 
        cvSaveImage(sys.argv[2], pImg2)
 
        # 创建窗口
 
        cvNamedWindow ("mywin")
 
        # 显示图像
 
        cvShowImage ("mywin", pImg)
        cvWaitKey (0)