import numpy as np

np.random.seed(42)

arr1 = np.random.randint(1, 100, size=(3, 3))
print(arr1)

arr2 = np.random.normal(0, 1, size=(4, 4))
print(arr2)

arr3 = np.eye(5)
print(arr3)

arr4 = np.random.normal(50, 10, size=(5, 4))
print(arr4)

arr5 = np.linspace(0, 1, 10)
print(arr5)

arr6 = np.random.choice([10, 20, 30], size=(2, 3))
print(arr6)