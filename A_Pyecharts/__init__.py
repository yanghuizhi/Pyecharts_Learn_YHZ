# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:42 下午

from flask import Blueprint

pyecharts_s=Blueprint('A_Pyecharts',__name__)

from A_Pyecharts.bar import view
from A_Pyecharts.bar import view2
from A_Pyecharts.bar import view3
