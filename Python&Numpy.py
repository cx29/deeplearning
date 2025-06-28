import numpy as np

# 这种初始化矩阵的方式有歧义，会生成（5，）类型的矩阵，不便于后续按照希望的方式计算
a = np.random.randn(5)

print(a)

# 这种明确标注行和列的才是我们所希望的初始化方式， 会生成（5，1）的矩阵,不会产生歧义
b = np.random.randn(5, 1)

print(b)
