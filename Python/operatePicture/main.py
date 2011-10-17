#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import operatingMethodCollection

if __name__ == '__main__':

    if len(sys.argv) == 2:
        inputFile = sys.argv[1]
    else:
        usage = 'Usage: python main.py [inputFileName]'
        print usage

        sys.exit(0)

    operateMethods = operatingMethodCollection.operationMethodCollection(inputFile)

    #operateMethods.convertToGray('grayCover.jpg',1)
    #operateMethods.operateCanny('cannyCover.jpg',1)
    operateMethods.detectEdge()
