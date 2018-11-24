import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
print(np.intersect1d(a, b))

c = np.random.randint(0, 25, 10)
sorted_c = np.sort(c)

print(c)
print(sorted_c)
c[c.argmax()] = 0
print(c)

multi_dim = np.random.randint(0, 25, [3, 3])
print(multi_dim)
print("-----------------------")
print(multi_dim.flatten())
print("-----------------------")
print(multi_dim.reshape([9]))
print("-----------------------")

matrix = np.random.randint(0, 25, [4, 4])
print(matrix)
print("-----------------------")
print(matrix - matrix.max(axis=1))
print("-----------------------")
fileMatrix = np.fromfile(file="matrix.txt", dtype=float, sep=';')
print("-----------------------")
print(fileMatrix + 1)
