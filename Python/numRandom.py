#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

dataset = ['mushroom.dat', 'pumsb.dat', 'chess.dat', 'connect.dat']
#dataset = ['data.txt']
def main():
	for data in dataset:
		print data
		with open(data) as fh:
			with open(data+"result.txt", 'a') as resultHandler:
				for line in fh.readlines():
					line = line.strip()
					lineArray = line.split(' ')
					for num in lineArray:
						# 生成一个0.6与1之间的随机浮点数
						randomNum = random.uniform(0.6, 1)
						resultHandler.write("%s %.3f "%(num, randomNum))
					resultHandler.write("\n")
                
if __name__ == '__main__':
    main()
