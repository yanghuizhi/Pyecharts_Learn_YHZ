import plotly.plotly as py

import numpy as np

data = [dict(

    visible=False,

    line=dict(color='#00CED1', width=6), # 配置线宽和颜色

    name='𝜈 = ' + str(step),

    x=np.arange(0, 10, 0.01), # x 轴参数

    y=np.sin(step * np.arange(0, 10, 0.01))) for step in np.arange(0, 5, 0.1)] # y 轴参数

data[10]['visible'] = True

py.iplot(data, filename='Single Sine Wave')
