# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:54 下午
import random
from flask import render_template, request
from A_bar import bar as bp
from pyecharts import options as opts
from pyecharts.charts import Bar

# 失败，没有成功，心累
# 柱状图2
# Flask 前后端分离
# http://127.0.0.1:5000/bar2?name=jerry&subtitle=Python教程

def bar_base2(name, subtitle) -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [random.randint(10, 100) for _ in range(6)])
            .add_yaxis("商家B", [random.randint(10, 100) for _ in range(6)])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=name, subtitle=subtitle))
    )
    return c

@bp.route("/bar2")
def bar2():
    data = request.args.to_dict()
    return render_template("A_Pyecharts/view2.html", result_json=data)

@bp.route("/barChart2")
def get_bar_chart2():
    args = request.args.to_dict()
    result = eval(args.get("result"))
    name = result.get("name")
    subtitle = result.get("subtitle")
    c = bar_base2(name,subtitle)

    return c.dump_options_with_quotes()


