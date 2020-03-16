# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 9:05 下午
import random
from pyecharts import options as opts
from pyecharts.charts import Page, Polar

def polar_scatter0() -> Polar:
    data = [(alpha, random.randint(1, 100)) for alpha in range(101)] # r = random.randint(1, 100)
    print(data)
    c = (
        Polar()
        .add("", data, type_="A_Pyecharts", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar"))
    )
    return c


polar_scatter0().render('./img/polar.html')
# 极坐标表示为(夹角,半径)，如(6,94)表示"夹角"为6，半径94的点：