# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:42 下午
from pyecharts.charts import Bar
import pyecharts.options as opts


# 柱状图1

attr = ["Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
      135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = {2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
      175.6, 182.2, 48.7, 18.8, 6.5, 2.3}

# 初始化一个bar对象(title,subtitle)
bar = (
    Bar()
    .add_xaxis(attr)
    .add_yaxis("蒸发1",v1,stack="stack1") # stack相同可产生堆叠效果
    .add_yaxis("蒸发2",v2,stack="stack2")
    # .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_series_opts(label_opts={"show": False})  # 等价上面配置
    .set_global_opts(title_opts=opts.TitleOpts(
        title="柱状图示例",subtitle="一年内蒸发和降水的折线图"))
)


bar.render("页面_Learn1.html")    # 生成本地 HTML 文件