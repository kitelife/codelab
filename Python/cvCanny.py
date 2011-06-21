# -*- coding:utf-8 -*-
###########################################################
# OpenCV example
#
# cvCanny：Canny边缘检测
#
# By ChaiShushan 2008
###########################################################
 
import sys
 
# 导入OpenCV模块
 
from opencv.cv import *
from opencv.highgui import *
 
if __name__ == '__main__':
 
    if len(sys.argv) == 2:
 
        # 载入图像，强制转化为Gray
        # 0表示Gray，1表示Origin，因为cvCanny函数参数要求图像必须是单通道的
 
        pImg = cvLoadImage(sys.argv[1], 0)
        if not pImg: sys.exit(-1)
 
        # 为canny边缘图像申请空间
 
        pCannyImg = cvCreateImage(cvGetSize(pImg), IPL_DEPTH_8U, 1)
 
        # canny边缘检测
        # 50和150是检测阀值，opencv必须手工输入阀值，如需自动匹配阀值参考cvCanny函数介绍
 
        cvCanny(pImg, pCannyImg, 50, 150, 3)
 
        # 创建窗口
 
        cvNamedWindow("src", 1)
        cvNamedWindow("canny",1)
 
        # 显示图像
 
        cvShowImage( "src", pImg )
        cvShowImage( "canny", pCannyImg )
 
        # 等待按键
 
        cvWaitKey(0); 
 
        # 销毁窗口
 
        cvDestroyWindow( "src" )
        cvDestroyWindow( "canny" )
 
        # 释放图像
 
        cvReleaseImage( pImg )
        cvReleaseImage( pCannyImg )
 
        sys.exit(0)