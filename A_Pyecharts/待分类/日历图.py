# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 9:04 下午

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


def calendar_interval_1() -> Calendar:
    begin = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 27)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range(0, (end - begin).days + 1, 2)  # 隔天统计
    ]

    calendar = (
        Calendar(init_opts=opts.InitOpts(width="1200px")).add(
            "", data, calendar_opts=opts.CalendarOpts(range_="2019"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2019年步数统计"),
            visualmap_opts=opts.VisualMapOpts(
                max_=25000,
                min_=1000,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return calendar


calendar_interval_1().render('./img/calendar.html')
print('ok')
# 绘制2019年1月1日到12月27日的步行数，官方给出的图形宽度900px不够，只能显示到9月份，本例使用opts.InitOpts(width="1200px")做出微调，并且visualmap显示所有步数，每隔一天显示一次：