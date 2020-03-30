# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
基础学习实践
    创建一个图像轴

"""

import matplotlib.pyplot as plt


# 基础
def FigureDemo(x,y):
    plt.figure()    # 创建一个对象
    plt.plot(x,y)   # 在当前绘图图像进行绘图，传入 x y
    _, ax = plt.subplots(2, 1)  # 创建一个 两行一列 的坐标图
    plt.show()  # 展示出来
    return print("调用完毕")

# pylab 常用在交互式的绘图
def pylabfun(x_data):
    y_data = [i * i for i in x_data]
    plt.plot(x_data, y_data, 'r*', label='example1')
    plt.plot(y_data, x_data, 'b*', label='example2')
    plt.legend()
    plt.show()
    return print("调用完毕")

FigureDemo(3,3)