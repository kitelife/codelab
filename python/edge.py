#! /usr/bin/env python
 
print "OpenCV Python version of edge"
 
import sys
 
# import the necessary things for OpenCV
from opencv import cv
from opencv import highgui
 
# some definitions
win_name = "Edge"
trackbar_name = "Threshold"
 
# the callback on the trackbar
def on_trackbar (position):
    #下面两句应该是没什么用的
    cv.cvSmooth (gray, edge, cv.CV_BLUR, 3, 3, 0)    #图像平滑
    cv.cvNot (gray, edge)     #计算数组元素的按位取反
 
    # run the edge dector on gray scale
    cv.cvCanny (gray, edge, position, position * 3, 3)   #采用 Canny 算法做边缘检测
 
    # reset
    cv.cvSetZero (col_edge)   #清空数组
 
    # copy edge points
    cv.cvCopy (image, col_edge, edge)   #参数edge影响拷贝的结果
 
    # show the image
    highgui.cvShowImage (win_name, col_edge)
 
if __name__ == '__main__':
    filename = "Fruits.jpg"
 
    if len(sys.argv)>1:
        filename = sys.argv[1]
 
    # load the image gived on the command line
    image = highgui.cvLoadImage (filename)
 
    if not image:
        print "Error loading image '%s'" % filename
        sys.exit(-1)
 
    # create the output image
    col_edge = cv.cvCreateImage (cv.cvSize (image.width, image.height), 8, 3)
 
    # convert to grayscale
    gray = cv.cvCreateImage (cv.cvSize (image.width, image.height), 8, 1)
    edge = cv.cvCreateImage (cv.cvSize (image.width, image.height), 8, 1)
    cv.cvCvtColor (image, gray, cv.CV_BGR2GRAY)
 
    # create the window
    highgui.cvNamedWindow (win_name, highgui.CV_WINDOW_AUTOSIZE)
 
    # create the trackbar
    highgui.cvCreateTrackbar (trackbar_name, win_name, 1, 100, on_trackbar)
 
    # show the image
    on_trackbar (0)
 
    # wait a key pressed to end
    highgui.cvWaitKey (0)