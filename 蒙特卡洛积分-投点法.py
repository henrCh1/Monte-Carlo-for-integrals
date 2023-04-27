# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:10:11 2023

@author: 86319
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 2*x + 1    # 定义被积函数

# 创建数据点
x = np.linspace(0, 10, 100)
y = f(x)

# 绘制图像
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 + 2x + 1')
plt.show()

a = 0    # 积分下限
b = 10   # 积分上限
N = 1000000    # 投点数

count = 0   # 落在函数图像下方的点的个数

for i in range(N):
    x = random.uniform(a, b)
    y = random.uniform(0, f(b))
    if y <= f(x):
        count += 1

integral = (b - a) * f(b) * count / N    # 计算积分值

print("积分结果: ", integral)
