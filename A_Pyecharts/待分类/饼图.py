# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 6:59 下午

# // 导入饼图Pie



# // 设置主标题与副标题，标题设置居中，设置宽度为900
from pyecharts.charts import Pie

pie = Pie()

# // 加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示

# pie.add("降水量", data_pair= /center=[25, 50] )

# // 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签

# pie.add("蒸发量", columns, data2, center=[75, 50], is_legend_show=False, is_label_show=True)
#
# // 保存图表

pie.render()