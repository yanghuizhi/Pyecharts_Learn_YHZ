# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 2:40 下午

import matplotlib.pyplot as plt


height=[161,170,182,175,173,165]
weight=[50,58,80,70,69,55]

# 画图
plt.scatter(height,weight , alpha=0.7)

plt.xlabel( 'X轴展示')  # x轴
plt.ylabel( 'Y轴展示')  # Y轴
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签

plt.title('标题')
plt.show()