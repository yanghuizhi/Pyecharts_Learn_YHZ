# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("F:/1/python/")  # 把自己的路径加入
import numpy as np
from Matplotlib_yhz import functioner as fc
from Matplotlib_yhz import basics
from Matplotlib_yhz import interesting



x = np.arange(0, 12, 1)  # 生成一个 0—12 的序列，步长 1
y = np.arange(0, 12, 1)  # 生成一个 0—12 的序列，步长 1
z = {"wo": 2, "ai": 4, "ni": 8}    # 字典
year = [1950,1970,1990,2010]       # 年份
pop = [2.519,3.692,5.263,6.972]    # 全球总人口（单位：10亿）

# 散点图,label好像不怎么管用，title也不管用
# fc.scatterplot1(x, y)
# fc.scatterplot2(x, y)
# fc.scatterplot3(year, pop)

# 折线图
# fc.lineplot1(x, y)
# fc.lineplot2(year, pop)

# 曲线图
# fc.curveplot1(x)
# fc.curveplot2(x_data=np.linspace(0, 10, 1000))

# 直方图，有问题
# fc.histogram(n_bins=3,data=z)

# 柱状图
# fc.barplot(x,y,error_data=8)
# fc.stackedbarplot(x_data=x,y_data=y,error_data=8)   # 有问题
# fc.groupedbarplot(x_data=x ,y_data_list=y,colors="r")   # 有问题

# 箱形图
# fc.boxplot(x,y)

# 初级学习
# basics.FigureDemo(x,y)
# basics.pylabfun(x)
# basics.zhexiantu(x,y)


# 图标个性化
# un = interesting.inter1()
# un = interesting.inter2(year, pop)

