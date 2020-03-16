# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/11 7:51 下午


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
print(plt.plot(x, np.sin(x)))


def reverseString(s):
    """
    Do notreturn anything, modify s in-place instead.
   """
    start = 0  # 队首
    end = len(s) - 1  # 队尾

    def reverse(s, start, end):
        if start >= end:  # start与end相遇的时候停止递归
            return

    s[start], s[end] = s[end], s[start]  # 交换位置
    reverse(s, start + 1, end - 1)  # 递归处理下一对start和end

    reverse(s, start, end)

ss=["h","e","l","l","o"]
print(reverseString(ss))