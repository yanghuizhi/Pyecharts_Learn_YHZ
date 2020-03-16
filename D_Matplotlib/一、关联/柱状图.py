# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 1:43 下午

import numpy as np
import matplotlib.pyplot as plt

# 柱的个数，生成一个数组，从0到4
index = np.arange(5)
#柱的高度
y=[20,10,30,25,15]

#  画图，生成5个高度为y，柱的宽度为0.5，颜色是红色的柱体
p1 = plt.bar(x=index, height=y , width=0.5 , color='r' )
# 添加图的标题
plt.title("bar demo")
plt.show()