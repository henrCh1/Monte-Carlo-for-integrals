# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:38:43 2023

@author: 86319
"""

def f(x):
    return x**2 + 2*x + 1    # 定义被积函数

a = 0    # 积分下限
b = 10   # 积分上限
N = 1000000    # 采样点数

m = 2**31 - 1   # 模数
a_c = 2023492103   # a常数
c_c = 12345   # c常数
x = 6789   # 初始种子

integral_sum = 0    # 积分值的累加和

for i in range(N):
    x = (a_c * x + c_c) % m    # 使用乘加同余法生成伪随机数
    u = x / m    # 将伪随机数映射到[0,1)区间
    y = a + u * (b - a)    # 将[0,1)区间内的伪随机数映射到[a,b]区间内
    integral_sum += f(y)    # 将该采样点的函数值加入积分和

integral = (b - a) * integral_sum / N    # 计算积分值

print("积分结果为: ", integral)
