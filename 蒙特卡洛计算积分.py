# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:36:17 2023

@author: 86319
"""

import random

def f(x):
    return x**2 + 2*x + 1    # 定义被积函数

a = 0    # 积分下限
b = 10   # 积分上限
N = 1000000    # 采样点数

integral_sum = 0    # 积分值的累加和

for i in range(N):
    x = random.uniform(a, b)    # 在积分区间内随机生成一个采样点
    integral_sum += f(x)    # 将该采样点的函数值加入积分和

integral = (b - a) * integral_sum / N    # 计算积分值

print("积分结果: ", integral)
