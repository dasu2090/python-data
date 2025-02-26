import numpy as np

#一次元配列
a = np.array([1,2,3])
print("a = np.array([1,2,3])")
print(a)
print(type(a))
print("a.shape")
print(a.shape)

print()

#二次元配列
b = np.array([[1,2,3], [4,5,6]])
print("b = np.array([[1,2,3], [4,5,6]])")
print(b)
print(type(b))
print("b.shape")
print(b.shape)

print()

#変形 reshape
c1 = np.array([0,1,2,3,4,5])
print("c1 = np.array([0,1,2,3,4,5])")
print(c1)
c2 = c1.reshape((2, 3))
print("c2 = c1.reshape((2, 3))")
print(c2)

print()

#一次元配列に変換
c3 = c2.ravel()
print("ravelは参照を返す")
print("c3 = c2.ravel()")
print(c3)

print()

c4 = c2.flatten()
print("flattenはコピーを返す")
print("c4 = c2.flatten()")
print(c4)
