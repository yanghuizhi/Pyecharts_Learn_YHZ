"""
matplotlib新姿势：让可视化图形动起来

其实matplotlib有一个少有人知的功能animation.FuncAnimation，可以接受你编写的动画函数创建动图。通过一个例子展示这一功能的用法，并介绍通过增强数据和高斯平滑，让动图更美观的技巧。

美国的过量服用海洛因致死数，使用seaborn创建

Python的matplotlib和seaborn是非常好用的绘图库。但它们创建的都是静态图像，难以通过动态、美观的方式描述数据值的变化。如果你的下一次演示或者下一篇博客文章，能用动态图形展示数据的发展，该有多好？更妙的是，你可以继续使用matplotlib、seaborn或者其他你喜欢用的库。

我最近为一部关于美国的阿片样物质危机的纪录片制作了一些动态图形，所以我会在这篇文章中使用相关的数据。

数据来自美国国家药物滥用研究所和CDC的公开数据，可以从以下网址下载：

https://www.drugabuse.gov/sites/default/files/overdose_data_1999-2015.xls

本文将使用matplotlib和seaborn绘制图形，同时使用numpy和pandas处理数据。matplotlib提供了一些可以用来制作动画的函数。闲话少叙，让我们开始吧，首先，是引入所有依赖。
"""

import numpy as np

import pandas as pd

import seaborn as sns

import matplotlib

import matplotlib.pyplot as plt

import matplotlib.animation as animation

# 然后我们加载数据，将其转换成pandas的DataFrame。我还编写了一个辅助函数，可以从感兴趣的行加载数据，之后绘图会用到。

overdoses = pd.read_excel('overdose_data_1999-2015.xls',sheetname='Online',skiprows =6)

def get_data(table,rownum,title):

    data = pd.DataFrame(table.loc[rownum][2:]).astype(float)

    data.columns = {title}

    return data
"""
准备就绪，下面是本文主要部分，如何绘制动画。

首先，如果你也和我一样，用的都是jupyter notebook，那么我建议你使用%matplotlib notebook指令，这样可以直接在notebook中查看动画效果，无需等待保存后再查看。

我使用了之前编写的辅助函数get_data取得海洛因服用过量数，并将其封装入一个两列的pandas DataFrame，一列表示年份，一列表示服用过量数。

%matplotlib notebook
"""
title = 'Heroin Overdoses'

d = get_data(overdoses,18,title)

x = np.array(d.index)

y = np.array(d['Heroin Overdoses'])

overdose = pd.DataFrame(y,x)

#XN,YN = augment(x,y,10)

#augmented = pd.DataFrame(YN,XN)

overdose.columns = {title}

# 接着我们初始化一个写入器（writer），基于ffmpeg记录20 fps（比特率为1800）。当然，你可以按照需要调整这些参数。

Writer = animation.writers['ffmpeg']

writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

# 接下来创建一个带标签的图形。别忘了限定x轴和y轴的范围，以免动画在显示数据时出现跳跃现象。

fig = plt.figure(figsize=(10,6))

plt.xlim(1999, 2016)

plt.ylim(np.min(overdose)[0], np.max(overdose)[0])

plt.xlabel('Year',fontsize=20)

plt.ylabel(title,fontsize=20)

plt.title('Heroin Overdoses per Year',fontsize=20)

# 制作动画的关键是定义一个动画函数，指定视频的每一帧发生了什么。这里i表示动画帧的索引。你可以选择在i帧中可见的数据范围。之后我使用seaborn的线图绘制选定数据。最后两行我调整了一些尺寸，使图形看起来更美观。

def animate(i):

    data = overdose.iloc[:int(i+1)]  # 选定数据范围

    p = sns.lineplot(x=data.index, y=data[title], data=data, color="r")

    p.tick_params(labelsize=17)

    plt.setp(p.lines,linewidth=7)

# 定义了动画函数后，使用

# matplotlib.animation.FuncAnimation定义动画应当包含多少帧，也就是说，通过frames参数定义调用animate(i)的频率。

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=17, repeat=True)

# 之后只需调用ani.save()就可以将动画保存为mp4文件。如果你想在保存之前先看下效果，那么可以使用plt.show()。

ani.save('HeroinOverdosesJumpy.mp4', writer=writer)

# 好了，让我们来看下效果。

# 看起来效果还可以，但是感觉有点抖动。为了缓解抖动的现象，我们可以在已有数据中插入一些中间值，平滑一下。为此我们定义以下的数据增强函数：

def augment(xold,yold,numsteps):

    xnew = []

    ynew = []

    for i in range(len(xold)-1):

        difX = xold[i+1]-xold[i]

        stepsX = difX/numsteps

        difY = yold[i+1]-yold[i]

        stepsY = difY/numsteps

        for s in range(numsteps):

            xnew = np.append(xnew,xold[i]+s*stepsX)

            ynew = np.append(ynew,yold[i]+s*stepsY)

    return xnew,ynew

# 之后我们只需在数据上应用这一增强函数，并相应地增加matplotlib.animation.FuncAnimation函数中的帧数。这里我调用augment函数时使用了参数numsteps=10，也就是说，我将数据点增加到160个，相应地，帧数设置为frames=160。增强数据之后，结果看起来平滑了很多，但在数据值变动处，曲线仍有一些尖角，看起来不是特别美观。

# 为了让图像看起来更美观，我们实现了一个高斯平滑函数：

def smoothListGaussian(listin,strippedXs=False,degree=5):  

    window=degree*2-1  

    weight=np.array([1.0]*window)  

    weightGauss=[]  

    for i in range(window):  

        i=i-degree+1  

        frac=i/float(window)  

        gauss=1/(np.exp((4*(frac))**2))  

        weightGauss.append(gauss)

    weight=np.array(weightGauss)*weight  

    smoothed=[0.0]*(len(listin)-window)  

    for i in range(len(smoothed)):
        smoothed[i]=sum(np.array(listin[i:i+window])*weight)/sum(weight)

    return smoothe

# 最后我们略微调整下颜色和风格，就得到了文章开头的动态图形：

sns.set(rc={'axes.facecolor':'lightgrey', 'figure.facecolor':'lightgrey','figure.edgecolor':'black','axes.grid':False})

