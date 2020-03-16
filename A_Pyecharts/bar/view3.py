# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:54 下午
import random
from flask import render_template, request
from A_bar import bar as bp
from pyecharts import options as opts
from pyecharts.charts import Bar


# 柱状图3
# 定时刷新，通过配置js文件

def bar_base3() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [random.randint(10, 100) for _ in range(6)])
            .add_yaxis("商家B", [random.randint(10, 100) for _ in range(6)])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="", subtitle=""))
    )
    return c

@bp.route("/bar3")
def bar3():
    return render_template("A_Pyecharts/view3.html")

@bp.route("/barChart3")
def get_bar_chart3():
    c = bar_base3()

    return c.dump_options_with_quotes()

