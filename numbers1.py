import numpy as np

a = np.zeros([10])
b = np.zeros([10])
b[3] = 4
c = np.full([10], 14.8)
d = np.arange(23, 39, 1)
e = np.flip(d)
f = np.arange(1, 10, 1)
g = np.reshape(f, [3, 3])
h = np.array([1, 2, 0, 0, 4, 0]).nonzero()
print(a)
print(b)
print(c)
print(d)
print(e)
print(g)
print(h)
