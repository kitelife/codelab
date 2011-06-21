# -*- coding:utf-8 -*-
 
import sys
 
# 导入OpenCV模块
 
from opencv.cv import *
from opencv.highgui import *
 
if __name__ == '__main__':
 
    # 打开图像
 
    image = cvLoadImage ("Lena.jpg")
 
    # 创建窗口
 
    cvNamedWindow ("mywin")
 
    # 显示图像
 
    cvShowImage ("mywin", image)
    cvWaitKey (0)
