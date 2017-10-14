# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from pylab import *

f = open("saber_temperature.txt")
index = 0
for line in f:
	index += 1
	rs = line.rstrip('\n')  # 移除行尾换行符
	rs = rs.split('\t')
	rs.pop(0)
	if index > 2 and index != 10 and index != 12:
		x = [0, 0.6, 1, 1.5, 14.5,15,16,17,19,19.5,20.5,21.5]
		ylim(0,100)
		plt.xlabel('time/hour')
		plt.ylabel('temperature')
		rs = [float(i) for i in rs]
		#print(rs)
		pl.plot(x, rs)
pl.show()