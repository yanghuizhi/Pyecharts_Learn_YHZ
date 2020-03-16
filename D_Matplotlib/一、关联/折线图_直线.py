# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 1:43 下午


import matplotlib.pyplot as plt
import numpy as np

# 生成等区间的Numpy数组ndarray，从-1到1分成50份。
x = np.linspace( -1 , 1, 50  )
#线程方程为y = 2x + 1
y = 2 * x + 1

# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y ')
# 画图
plt.plot(x,y)
# 图形显示
plt.show()
