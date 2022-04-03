from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def fun(a, b):
    """
     fun = a^2 + b^2
    :param a:
    :param b:
    :return:
    """
    return a ** 2 + b ** 2


# 创建一个新的matplotlib.figure.Figure并为其添加一个类型为Axes3D的新轴
fig = plt.figure()
ax = Axes3D(fig)
# 生成数据
x = np.arange(-1.5, 1.5, 0.1)  # 从-3到3单位间隔为0.2
y = np.arange(-1.5, 1.5, 0.1)  # 从-3到3单位间隔为0.2
x, y = np.meshgrid(x, y)  # 初始散点数据处理成xy网格数据
f = fun(x, y)  # 函数调用
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f')
# 标题名称、位置：0左下，1右上
ax.text2D(0.3, 0.95, "f(x, y) = x^2 + y^2", transform=ax.transAxes)
ax.plot_surface(x, y, f)
plt.savefig("pic.png")
plt.show()
