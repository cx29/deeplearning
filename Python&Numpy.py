import numpy as np

# 这种初始化矩阵的方式有歧义，会生成（5，）类型的数组，不便于后续按照希望的方式计算
a = np.random.randn(5)  # ≈a.shape=(5,) 秩为1的矩阵

print(a)

# 这种明确标注行和列的才是我们所希望的初始化方式， 会生成（5，1）的矩阵,不会产生歧义
b = np.random.randn(5, 1)

print(b)

# 使用断言来检查并确保b的形状为所需要的矩阵
assert (b.shape == (5, 1))  # 调试语句

# 如果得到了一个秩为1的数组, 可以通过重新定义形状的方式来使数组改变为希望的形状
a = a.reshape(5, 1)
print(a)
