#!/usr/bin/env python

#-*- coding: utf-8 -*-
import sys
from opencv.cv import *
from opencv.highgui import *

class operationMethodCollection():

    def __init__(self,input):
        self.inputFile = input

    def convertToGray(self, outputFile, flag):
        grayImg = cvLoadImage(self.inputFile, 0)

        if flag == 1:
            cvSaveImage(outputFile, grayImg)
        else:
            windowName = 'imgWin'
            cvNamedWindow (windowName)
            cvShowImage(windowName, grayImg)
            cvWaitKey(0)
            
        return grayImg

    def operateCanny(self, outputFile, flag):
        pImg = self.convertToGray(outputFile,0)
        pCannyImg = cvCreateImage(cvGetSize(pImg), IPL_DEPTH_8U, 1)
        cvCanny(pImg, pCannyImg, 50, 150, 3)

        if flag == 1:
            cvSaveImage(outputFile, pCannyImg)
        else:
            windowName = 'imgWin'
            cvNamedWindow (windowName)
            cvShowImage(windowName, pCannyImg)
            cvWaitKey(0)

        return pCannyImg

    def copyImg(self, outputFile):
        pImg = cvLoadImage(self.inputFile, 1)
        if not pImg:
            sys.exit(-1)
        pImg2 = cvCreateImage(cvGetSize(pImg), pImg.depth, pImg.nChannels)
        cvCopy(pImg, pImg2, None)
        cvSaveImage(outputFile,pImg2)

    def detectEdge(self):

        win_name = "Edge"
        trackbar_name = "Threshold"

        pImg = cvLoadImage (self.inputFile)
        if not pImg:
            print "Error loading image '%s'" % self.inputFile
            sys.exit(-1)

        # create the output image
        col_edge = cvCreateImage (cvSize (pImg.width, pImg.height), 8, 3)

        # convert to grayscale
        gray = cvCreateImage (cvSize (pImg.width, pImg.height), 8, 1)
        edge = cvCreateImage (cvSize (pImg.width, pImg.height), 8, 1)
        cvCvtColor (pImg, gray, CV_BGR2GRAY)

        # create the window
        cvNamedWindow (win_name, CV_WINDOW_AUTOSIZE)

        def on_trackbar(position):
            cvSmooth (gray, edge, CV_BLUR, 3, 3, 0)
            cvNot (gray, edge)
            # run the edge dector on gray scale
            cvCanny (gray, edge, position, position * 3, 3)
            # reset
            cvSetZero (col_edge)
            # copy edge points
            cvCopy (pImg, col_edge, edge)
            # show the image
            cvShowImage (win_name, col_edge)

        # create the trackbar
        cvCreateTrackbar (trackbar_name, win_name, 1, 100, on_trackbar)

        # show the image
        on_trackbar (0)

        # wait a key pressed to end
        cvWaitKey (0)