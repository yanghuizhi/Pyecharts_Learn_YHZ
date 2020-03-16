# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:42 下午


from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

"""
        pyecharts Bar 主要配置学习
"""


def bar_border_radius():
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts( # 柱状图显示效果动画控制代码
                    animation_delay=500,
                    animation_easing="cubicOut"
                ),
                theme=ThemeType.MACARONS,  # 柱状图显示主题
                page_title="Bar Learn",    # 设置html页面标题
            )
        )
        # .reversal_axis()  # 翻转XY轴
        .add_xaxis(["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"])
        .add_yaxis("A", Faker.values(),
                   category_gap="50%",  # 柱间距对应的控制代码
                   markpoint_opts=opts.MarkPointOpts(),
                   is_selected=True  # A系列柱子是否显示对应的控制代码
                   )
        .set_global_opts(
            title_opts=opts.TitleOpts(  # 标题
                    title="Bar-参数使用例子",
                    subtitle="副标题"
            ),
            toolbox_opts=opts.ToolboxOpts(),  # toolbox 工具箱配置
            yaxis_opts=opts.AxisOpts(position="right", name="Y轴"), # Y轴右侧控制
            datazoom_opts=opts.DataZoomOpts(),  # 数据区域放大缩小设置
        )
        .set_series_opts(
            itemstyle_opts={  # A系列柱子颜色渐变对应的控制代码
                "normal": {
                    "color": JsCode("""
                        new echarts.graphic.LinearGradient(
                        0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'}, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'}], false)"""
                    ),
                    "barBorderRadius": [6, 6, 6, 6],
                    "shadowColor": 'rgb(0, 160, 221)',
                }
            },
            # A系列柱子最大和最小值标记点对应的控制代码
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            # A系列柱子最大和最小值标记线对应的控制代码
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            )
        )
    )

    return c

# 生成本地 HTML 文件, 可指定文件名字
bar_border_radius().render("页面_Learn2.html")