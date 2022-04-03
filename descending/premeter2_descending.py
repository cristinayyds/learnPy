
# -*- coding: utf-8 -*-
"""
二维问题的梯度下降法示例
"""
import math
import numpy as np


def func_2d(x):
    """
    目标函数
    :param x: 自变量，二维向量
    :return: 因变量，标量
    """
    return - math.exp(-(x[0] ** 2 + x[1] ** 2))


def grad_2d(x):
    """
    目标函数的梯度
    :param x: 自变量，二维向量
    :return: 因变量，二维向量
    """
    deriv0 = 2 * x[0] * math.exp(-(x[0] ** 2 + x[1] ** 2))
    deriv1 = 2 * x[1] * math.exp(-(x[0] ** 2 + x[1] ** 2))
    return np.array([deriv0, deriv1])


def gradient_descent_2d(grad, cur_x=np.array([0.1, 0.1]), learning_rate=0.01,
                        precision=0.0001, max_iters=10000):
    """
    二维问题的梯度下降法
    :param grad: 目标函数的梯度
    :param cur_x: 当前 x 值，通过参数可以提供初始值
    :param learning_rate: 学习率，也相当于设置的步长
    :param precision: 设置收敛精度
    :param max_iters: 最大迭代次数
    :return: 局部最小值 x*
    """
    print("f{cur_x} 作为初始值开始迭代...")
    for i in range(max_iters):
        grad_cur = grad(cur_x)
        if np.linalg.norm(grad_cur, ord=2) < precision:
            break  # 当梯度趋近为 0 时，视为收敛
        cur_x = cur_x - grad_cur * learning_rate
        print("第", i, "次迭代：x 值为 ", cur_x)

    print("局部最小值 x =", cur_x)
    return cur_x


if __name__ == '__main__':
    gradient_descent_2d(grad_2d, cur_x=np.array([1, -1]), learning_rate=0.2, precision=0.000001, max_iters=10000)

'''
@ 梯度下降法实现简单，原理也易于理解，但它有自身的局限性，因此有了后面很多算法对它的改进。

@ 对于梯度过小的情况，梯度下降法可能难以求解。

@ 此外，梯度下降法适合求解只有一个局部最优解的目标函数，对于存在多个局部最优解的目标函数，一般情况下梯度下降法不保证得到全局最优解（由于凸函数有个性质是只存在一个局部最优解，所有也有文献的提法是：当目标函数是凸函数时，梯度下降法的解才是全局最优解）

'''