# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import xlrd
from pylab import *

data = xlrd.open_workbook('saber_temperature_continue.xlsx')
table = data.sheet_by_index(0) #获得第一个工作表
nrows = table.nrows #行数
ncols = table.ncols #列数

ylim(0,50)
plt.xlabel('time/s')
plt.ylabel('temperature')

for i in range(1,nrows):
	y = table.row_values(i)
	y.pop(0)
	x = range(20)
	pl.plot(x, y)
pl.show()