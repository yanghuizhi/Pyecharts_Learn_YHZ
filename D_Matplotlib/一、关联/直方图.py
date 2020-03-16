# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 3:08 下午
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.random.randn(200)
s = pd.Series(a)

plt.hist(s)
plt.show()