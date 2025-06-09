import numpy as np
import time

a = np.random.rand(1000000)  # 生成随机向量
b = np.random.rand(1000000)

# 记录当前时间
tic = time.time()

c = np.dot(a, b)  # 进行向量点积运算(求和从1到最后的每一个a*b) 底层使用C来实现

toc = time.time()

print("Vectorization version:" + str(1000 * (toc - tic)) + "ms")

c = 0

tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print("No-Vectorization version:" + str(1000 * (toc - tic)) + "ms")
c = 0
tic = time.time()
