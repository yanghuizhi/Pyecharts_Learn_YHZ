# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 1:43 下午
import numpy as np
import matplotlib.pyplot as plt

N = 5
# 柱的高度
y=[20,10,30,25,15]
# 柱的个数
index = np.arange(N)

#  画图，生成5个高度为y，方向是水平的，柱的宽度为0.8，颜色是蓝色的柱体
p2 = plt.bar(x=0,bottom=index, width=y,height=0.8,orientation ='horizontal' )
# 添加图的标题
plt.title("bar demo")
plt.show()