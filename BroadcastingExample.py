import numpy as np

A = np.array([
    [56.0, 0.0, 4.4, 68.0],
    [1.2, 105, 52, 68.0],
    [56.0, 0.0, 4.4, 68.0],
    [56.0, 0.0, 4.4, 68.0],
])

print(A)

# 按照垂直方向进行求和
cal = A.sum(axis=0)  # 1为水平方向

print(cal)

# 计算百分比, 这里就是广播的例子
# reshape消耗时间O(1)
percentage = 100 * A / cal.reshape(1, 4)  # 使用矩阵A除以了cal这个1行4列的矩阵，得到百分比矩阵
print(percentage)
