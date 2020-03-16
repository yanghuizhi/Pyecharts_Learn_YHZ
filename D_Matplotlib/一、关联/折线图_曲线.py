# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 1:43 下午


import matplotlib.pyplot as plt
import numpy as np

# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y ')

# 取5个点可以看到折线的效果
#x = np.linspace( -1 , 1, 5 )
x = np.linspace( -1 , 1, 50  )

# 线程方程为y = x ** 2
y = x**2

# 画图
plt.plot (x,y)
# 图形显示
plt.show()