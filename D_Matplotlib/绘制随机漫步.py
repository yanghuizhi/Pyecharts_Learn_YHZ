# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/16 2:04 下午
import matplotlib.pyplot as plt
from random import choice
import random
class RandomWalk():
    def __init__(self, num_point=5000):
        self.num_point = num_point

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):

        while len(self.x_value) < self.num_point:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


if __name__ == '__main__':
    rw = RandomWalk(10000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6),dpi=100)
    plt.scatter(rw.x_value, rw.y_value, s=1, c=rw.y_value, cmap=plt.cm.Reds)
    plt.scatter(0,0,s=15,c='black')
    plt.scatter(rw.x_value[-1],rw.y_value[-1],s=15, c='blue')
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

# plt.scatter(b,a,s=15,edgecolors='none',c='red')
# plt.scatter(b,b, s=15, edgecolors='none', c=b,cmap=plt.cm.Blues)
# plt.plot(a, linewidth=2)
# plt.title('a', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('y', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
    plt.show()
    plt.savefig('random_walk.png')