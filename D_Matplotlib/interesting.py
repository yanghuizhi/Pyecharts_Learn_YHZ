# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def inter1():
    x=np.linspace(0,10,500)
    dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

    fig, ax = plt.subplots()
    line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                     label='Dashes set retroactively')
    line1.set_dashes(dashes)

    line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                     label='Dashes set proactively')

    ax.legend(loc='lower right')
    # plt.savefig("testimage.jpg")
    plt.show()


def inter2(x_data, y_data):
    # 图标标题
    plt.title('World Polulation')

    # x,y轴名称

    plt.xlabel('Year')

    plt.ylabel('Polulation')

    # y轴刻度，第二个参数为显示的刻度

    plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

    # 填充曲线下方区域

    plt.fill_between(x_data,y_data,0,color = 'green')

    plt.show()