import numpy as np

r = np.random.random([10, 10])
mm = np.random.randint(0, 25, [15])

random = np.random.random([30])
h = random.mean(keepdims=False)
o = np.reshape(random, [3, 10])
pad = np.pad(o, 1, 'constant', constant_values=0)
leftMatrix = np.random.random([5, 3])
rightMatrix = np.random.random([3, 2])
product = leftMatrix.dot(rightMatrix)


print(r.max())
print(r.min())
print(mm.argmax())
print(mm.argmin())
print(h)
print(random)
print(o.mean(axis=0, keepdims=True))
print(o.mean(axis=1, keepdims=True))
print(pad)
print(product)
