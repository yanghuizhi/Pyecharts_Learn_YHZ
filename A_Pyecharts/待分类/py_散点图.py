# from pyecharts import Polar

import random

from pyecharts.charts import Polar

data_1 = [(10, random.randint(1, 100)) for i in range(300)]

data_2 = [(11, random.randint(1, 100)) for i in range(300)]

polar = Polar()

polar.add("", data_1, )

polar.add("", data_2,)

polar.render("pyhtml_生成的散点图.html")
