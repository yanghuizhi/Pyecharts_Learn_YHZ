# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 1:45 下午

import matplotlib.pyplot as plt  # 导入
import numpy as np
from matplotlib import pyplot as plt

from matplotlib import font_manager

# 解决中文乱码

# plt.rcParams['font.sans-serif'] = ['SimHei']

# plt.rcParams['font.serif'] = ['SimHei']

# 设置字体

# my_font = font_manager.FontProperties()

# 设置画布大小

plt.figure(figsize=(20,10),dpi=80)

# 每个名称和分数，必须一一对应

a = ["小张","小李","小王","小赵","小孙","小钱","小武","小郑","小冯","小码"]

b=[55,80,75,90,82,30,42,99,54,66]

# 条形图

plt.bar(a,b, align='center',color='orange',alpha=0.8)

# x轴刻度

plt.xticks(range(len(a)),a,rotation=0)

# fontproperties=my_font)

# 绘制网格

plt.grid(alpha=0.2,color="#cccccc")

# 设置y轴范围

plt.ylim([0,100])

# 设置标题

plt.ylabel("姓名")

plt.xlabel("分数")

plt.title("姓名分数条形图")
# 显示图形

plt.show()