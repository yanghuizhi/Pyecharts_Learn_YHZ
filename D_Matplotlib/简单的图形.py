# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd     # 基于Numpy构建的，是Numpy的升级版本
import numpy as np      # 经常用于数据生成和一些运算
import matplotlib.pyplot as plt     # Python中强大的绘图工具

# 随机生成1000个数据
data = pd.Series(np.random.randn(10), index=np.arange(10))
# 为了方便观看效果, 我们累加这个数据
data.cumsum()
# pandas 数据可以直接观看其可视化形式
data.plot()
plt.show()
