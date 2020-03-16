# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 2:40 下午

import numpy as np
import matplotlib.pyplot as plt


#设置随机数种子
np.random.seed(10)
#使用Numpy的随机函数，产生X轴和Y轴的数据，具有相同长度的数据
N= 100
x = np.random.randn(N)
y1=np.random.randn(N)
#画图
plt.scatter(x,y1 )
# 图形显示
plt.show()