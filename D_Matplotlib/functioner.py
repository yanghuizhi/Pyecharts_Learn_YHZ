# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
图形方法：

    散点图：    非常适合展示两个变量之间的关系
    折线图：    非常适合一个变量随着另一个变量明显变化的时候，比如说它们有一个大的协方差。
    曲线图：    曲线图
    直方图：    查看（或真正地探索）数据点的分布是很有用的
    柱状图：    较少的数据进行分类可视化
    箱形图：    比直方图更多的信息
"""
import matplotlib.pyplot as plt
import numpy as np


# 创建散点图
def scatterplot1(x_data, y_data, x_label="x label", y_label="x label", title="设置默认抬头", color="r"):

    fig, ax = plt.subplots()  # 创建项目,返回一个object和坐标轴图像
    ax.scatter(x_data, y_data, s=60, color=color, alpha=0.75)  # 绘制数据，设置点的大小、颜色和透明度(alpha)

    ax.set_ylabel("logging")
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.show()
    return print("我是散点图")


def scatterplot2(x_data, y_data, x_label="x label", y_label="x label", title="设置默认抬头", color="r"):

    plt.figure()
    _, ax = plt.subplot(1, 1, 1)

    ax.plot(x_data, y_data, 'o', color='r')  # 传入坐标轴、曲线类型(查看api)、颜色
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)  # 标题
    plt.show()
    return print("我是散点图")

def scatterplot3(x_data, y_data, title="设置默认抬头"):

    plt.scatter(x_data, y_data)  # year:x轴，pop:y轴

    plt.show()
    return print("最简单的散点图")


# 折线图
def lineplot1(x_data, y_data, x_label="x label", y_label="x label", title="设置默认抬头"):
    _, ax = plt.subplots()  # 设置线条宽度、颜色和透明度(alpha)

    ax.plot(x_data, y_data, lw=2, color='red', alpha=1)  # 绘制最合适的线条，设置线条宽度(lw)、颜色和透明度(alpha)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # 解决绘图时中文显示为方块的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']    # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False      # 解决负号显示为方块的问题

    plt.show()
    return print("这是折线图第一种学习方式")


def lineplot2(x_data, y_data, title="设置默认抬头"):

    plt.plot(x_data, y_data)  # year:x轴，pop:y轴

    plt.show()
    return print("最简单的折线")


# 曲线图
def curveplot1(x):
    plt.plot(x, x, label='第一条线')  # 画3个数据图,可以按照格式举一反三
    plt.plot(x, x ** 2, label='第二条线')
    plt.plot(x, x ** 3, label='第三条线')

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.legend()  # 显示图例
    plt.show()


def curveplot2(x_data, x_label="x label", y_label="x label", title="默认标题"):
    y_data = np.sin(x_data)
    # 创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
    plt.figure(figsize=(8, 4))

    # 在当前绘图对象中画图（x轴,y轴,给所绘制的折线的名字，画线颜色，画线宽度）
    plt.plot(x_data, y_data, label="$sin(x)$", color="red", linewidth=2)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(-5, 12)     # 设置 x 轴的范围
    plt.xlim(1, 12)      # 设置 y 轴的范围

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.legend()    # 图示
    # plt.savefig("实例2.png")  # 保存图
    plt.show()

    return print("这是曲线图第二种学习方式")


# 直方图
# 参数 n_bins 控制我们想要在直方图中有多少个离散的组。
# cumulative 是一个布尔值，允许我们选择直方图是否为累加的，
#    基本上就是选择是 PDF（Probability Density Function，概率密度函数）
#    还是 CDF（Cumulative Density Function，累积密度函数）。
def histogram(data, n_bins, cumulative=False, x_label="", y_label="", title="设置默认抬头"):
    _, ax = plt.subplots()

    ax.hist(data, n_bins=n_bins, cumulative=cumulative, color='#539caf')

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # plt.savefig("实例2.png")  # 保存图
    plt.show()


# 覆盖2个直方图进行比较,使用不同的透明度去设置
def overlaid_histogram(data1, data2, n_bins = 0, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0", x_label="", y_label="", title=""):
    print("有问题")
    # Set the bounds for the bins so that the two distributions are fairly compared
    #
    # max_nbins = 10
    #
    # data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    #
    # binwidth = ((data_range[1] - data_range[0]) / max_nbins if n_bins == 0:
    #     bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)    else:
    #     bins = n_bins    # Create the plot
    #
    # _, ax = plt.subplots()
    #
    # ax.hist(data1, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    #
    # ax.hist(data2, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    #
    # ax.set_ylabel(y_label)
    #
    # ax.set_xlabel(x_label)
    #
    # ax.set_title(title)
    #
    # ax.legend(loc = 'best')


# 柱状图
def barplot(x_data, y_data, error_data, x_label="", y_label="", title=""):

    _, ax = plt.subplots()

    # Draw bars, position them in the center of the tick mark on the x-axis

    ax.bar(x_data, y_data, color = '#539caf', align = 'center')

    # Draw error bars to show standard deviation, set ls to 'none'

    # to remove line between points

    ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)

    ax.set_ylabel(y_label)

    ax.set_xlabel(x_label)

    ax.set_title(title)
    plt.show()

def stackedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="", y_label="", title=""):

    _, ax = plt.subplots()

    # Draw bars, one category at a time

    for i in range(0, len(y_data_list)):

        if i == 0:

            ax.bar(x_data, y_data_list[i], color = colors[i], align = 'center', label = y_data_names[i])

        else:

            # For each category after the first, the bottom of the

            # bar will be the top of the last category

            ax.bar(x_data, y_data_list[i], color = colors[i], bottom = y_data_list[i - 1], align = 'center', label = y_data_names[i])

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    ax.legend(loc = 'upper right')


def groupedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="", y_label="", title=""):

    _, ax = plt.subplots()

    # Total width for all bars at one x location

    total_width = 0.8

    # Width of each individual bar

    ind_width = total_width / len(y_data_list)

    # This centers each cluster of bars about the x tick mark

    alteration = np.arange(-(total_width/2), total_width/2, ind_width)

    # Draw bars, one category at a time

    for i in range(0, len(y_data_list)):

        # Move the bar to the right on the x-axis so it doesn't

        # overlap with previously drawn ones

        ax.bar(x_data + alteration[i], y_data_list[i], color = colors[i], label = y_data_names[i], width = ind_width)

    ax.set_ylabel(y_label)

    ax.set_xlabel(x_label)

    ax.set_title(title)

    ax.legend(loc = 'upper right')


# 箱形图
def boxplot(x_data, y_data, base_color="#539caf", median_color="#297083", x_label="", y_label="", title=""):

    _, ax = plt.subplots()

    # Draw boxplots, specifying desired style

    ax.boxplot(y_data

               # patch_artist must be True to control box fill

               , patch_artist = True

               # Properties of median line

               , medianprops = {'color': median_color}

               # Properties of box

               , boxprops = {'color': base_color, 'facecolor': base_color}

               # Properties of whiskers

               , whiskerprops = {'color': base_color}

               # Properties of whisker caps

               , capprops = {'color': base_color})

    # By default, the tick label starts at 1 and increments by 1 for

    # each box drawn. This sets the labels to the ones we want

    ax.set_xticklabels(x_data)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

    plt.show()