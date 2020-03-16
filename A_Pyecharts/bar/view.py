# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:54 下午
from markupsafe import Markup

from A_Pyecharts import pyecharts_s as bp
from pyecharts import options as opts
from pyecharts.charts import Bar


# 柱状图1
@bp.route('/bar1')
def bar1() -> Bar:
    bar=Bar()  # instantiation
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    bar.add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
        title="柱状图基本事例",
        subtitle="我是副标题"))

    return Markup(bar.render_embed())
