# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:41 下午
from random import randrange

from flask import render_template

from A_Pyecharts.待分类 import main as app

from pyecharts.charts import Line

# 失败，没有成功
def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

@app.route("/")
def index():
    return render_template("zhexian/index.html")

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

idx = 9

@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})