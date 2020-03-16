# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 9:05 下午
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


words = [
    ("Python", 100),
    ("C_test++", 80),
    ("Java", 95),
    ("R", 50),
    ("JavaScript", 79),
    ("C_test", 65)
]


def wordcloud() -> WordCloud:
    c = (
        WordCloud()
        # word_size_range: 单词字体大小范围
        .add("", words, word_size_range=[20, 100], shape='cardioid')
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"))
    )
    return c


wordcloud().render('./img/wordcloud.html')

# ("C_test",65)表示在本次统计中C语言出现65次