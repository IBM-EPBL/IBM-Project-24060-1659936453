import numpy as np
a = np.array([1, 2, 3])
print(a)
b = np.array([4, 5, 6])
print(b)
print('\n---Result of a and b---')
print(np.concatenate((a, b)))
