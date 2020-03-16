# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 7:41 下午

from pyecharts import options as opts  # 图表配置
from pyecharts.charts import Geo  # 地理坐标系
from pyecharts.faker import Faker
from pyecharts.globals import ChartType, SymbolType

# 这种方式叫做链式调用，使代码更加简洁。
# 方案一号
# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(),
#         title_opts=opts.TitleOpts(title="Geo-基本示例"),
#     )
# )
# c.render_notebook() # 显示地图，在notebook中直接展示图表
# c.render()# 输出html格式

# 学习
# add_schema() ：控制地图类型、视角中心点等
# add()：添加图表名称、传入数据集、选择geo图类型、调整图例等
# set_series_opts() ：系列配置项，可配置图元样式、文字样式、标签样式、点线样式等
# set_global_opts() ：全局配置项，可配置标题、动画、坐标轴、图例等
# render_notebook() ：在notebook中渲染显示图表
# add_coordinate() : 新增一个坐标点
# add_coordinate_json() ：以json形式新增多个坐标点
# get_coordinate() ：根据地点查询对应坐标


# 方案二号
# d = (
#         Geo()
#         .add_schema(maptype="北京")
#         .add(            "geo",
#             [list(z) for z in zip(['大兴区','房山区','海淀区','朝阳区','东城区'], [150,100,300,200,500])],
#             type_=ChartType.EFFECT_SCATTER,
#         )
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#             visualmap_opts=opts.VisualMapOpts(),
#             title_opts=opts.TitleOpts(title="Geo-HeatMap"),
#         )
#     )
#
# d.render_notebook()


# 方案三号,动态展示
# pyecharts可以生成地理空间流动图，用来表示航班数量、人口流动等等。
# 下面以全国主要城市航班流动图为例（虚拟数据）：
c = (
        Geo()
        .add_schema(maptype="china")
        .add(            "",
            [("深圳", 120), ("哈尔滨", 66), ("杭州", 77), ("重庆", 88), ("上海", 100), ("乌鲁木齐", 30),("北京", 30),("武汉",70)],
            type_=ChartType.EFFECT_SCATTER,
            color="green",
        )
        .add(            "geo",
            [("北京", "上海"), ("武汉", "深圳"),("重庆", "杭州"),("哈尔滨", "重庆"),("乌鲁木齐", "哈尔滨"),("深圳", "乌鲁木齐"),("武汉", "北京")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="全国主要城市航班路线和数量"))
    )

c.render()