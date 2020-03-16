# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/15 12:42 下午
from flask import Flask

app = Flask(__name__)

# pycharte学习
from A_Pyecharts import bar as bar_blueprint
app.register_blueprint(bar_blueprint)

from A_Pyecharts.待分类 import main as main_blueprint
app.register_blueprint(main_blueprint)

# B 系列，都是



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
