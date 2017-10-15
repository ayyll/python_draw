# 前言 #
某天felix要测saber的温度(saber是一款AR产品的手柄)，叫我20分钟去读一次，共十只，读上个一天，以便能绘出温度曲线。(简直不当人，一干就是一天) 

然后就是我巴拉巴拉跑一天腿给他测到数据，最后实在无聊，不如用python绘个图玩玩吧，所以有了这篇文章。

# 快速绘图 #

绘图主要用到matplotlib这个包，pip安装或者下载了手动安装都可以，其中有许多依赖包，根据报错信息依次安装即可。

使用时需要引入如下包：

```
import numpy as np
import pylab as pl
from pylab import *
```

## 折线图 ##

可以根据给定的x，y坐标快速绘制折线图：

```
import numpy as np
import pylab as pl
from pylab import *

x = [0, 1, 2, 3]
y = [0, 1, 2, 3]
pl.plot(x, y)
pl.show()
```

## 坐标范围 ##

可以手动限制x，y坐标的范围：

```
xlim(xmin, xmax)
ylim(ymin, ymax)
```

或者这样：

```
plt.axis([xmin, xmax, ymin, ymax])
```

## 坐标名称 ##

可以分别给x，y坐标添加名称：

```
plt.xlabel('x')
plt.ylabel('y')
```

## 添加图题 ##

默认是不支持中文的，添加图题可以这样：

```
plt.title('picture_name')
```

如果想支持中文，需要如下设置：

```
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```



参考资料：[matplotlib 绘图可视化知识点整理](http://python.jobbole.com/85106/)