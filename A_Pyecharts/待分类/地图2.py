# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 8:59 下午
from pyecharts import options as opts
from pyecharts.charts import Map

nums = [59989, 1328, 1257, 1172, 1007, 982, 933, 629, 553, 543, 508, 464, 387, 333, 302, 292, 242, 240, 172, 163, 146, 130, 127, 121, 91, 89, 76, 73, 70, 61, 22, 18, 10, 1]
provinces = ['湖北', '广东', '河南', '浙江', '湖南', '安徽', '江西', '江苏', '重庆', '山东', '四川', '黑龙江', '北京', '上海', '河北', '福建', '广西', '陕西', '云南', '海南', '贵州', '山西', '天津', '辽宁', '甘肃', '吉林', '新疆', '内蒙古', '宁夏', '香港', '台湾', '青海', '澳门', '西藏']
sequence = [(a,b) for a,b in zip(provinces,nums)]

mymap = Map()
mymap.add(series_name='中国最新疫情地图', data_pair=sequence, maptype='china')
mymap.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(pieces=[
                                        {"min": 1, "max": 9, "label": "1-9", "color": 'lightcoral'},
                                        {"min": 10, "max": 99, "label": "10-99", "color": 'indianred'},
                                        {"min": 100, "max":999, "label": "100-999", "color": 'brown'},
                                        {"min": 1000, "max": 9999, "label": "1000-9999", "color": 'firebrick'},
                                        {"min": 10000, "max": 60000, "label": "≥10000", "color":  'darkred'}],
                                        is_piecewise=True)
        )

mymap.render('地图2.html')