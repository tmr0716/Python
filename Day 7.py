print('----------------------------------- Classroom Day 7 -----------------------------------')
import numpy as np
# print('==================================== NUMPY LIBRARY ====================================')
# a = np.array([1, 2, 3, 4, 5])*2
# print(a)
# z = np.zeros((2, 3))
# print(z) # 2 rows, 3 columns all elements are zero
# n = np.ones((2, 3))
# print(n)
# print('==================================== BROADCASTING ====================================')
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9], [10, 11, 12]])
# c = a + b
# print(c)
# a = np.array([1, 2, 3])
# b = np.array([[10],
#                [20],
#                 [30]])
# c = a + b
# print(c)
# print('==================================== MATRIX/DETERMINANTS ====================================')
# a = np.array([[1, 2], [5, 7]])
# print(a)
# det = np.linalg.det(a)
# print(det)

# a = np.array([[1, 2],
#           [3, 4]])
# det = np.linalg.det(a)
# print("Determinant:")
# print(det)
# inv = np.linalg.inv(a)
# print("Inverse:")
# print(inv)

# a = np.array([[1, 2], [5, 7]])
# d = np.linalg.inv(a)
# print(d)
# p = a @ d
# print(p)

# print('======================================= VECTORIZED OPERATIONS FOR SPEED =======================================')
# x = np.linspace(0, 10, 1000)
# y_loop = []
# for xi in x:
#     y_loop.append(np.sin(xi) + np.cos(xi))
# y_vec = np.sin(x) + np.cos(x)
# print(y_vec)

# x = np.linspace(0, 4, 200)
# print(x)
# y = []
# for x_i in x:
#     y.append(int(np.sin(x_i) + int(np.cos(x_i))))
# print(y)
# y_arr = np.append(x,y)
# print(y_arr)

# print('==================================== MATRIX/DETERMINANTS ====================================')
# x  = np.array([1, 2, 3, 4, 5])
# y = np.array([[1, 2, 3, 4, 5], [4, 6, 67, 3, 0], [76, 89, 32, 1, 0]])
# z = x*y
# print(z)
# print('==================================== SLICING ====================================')
# arr = np.array([1, 2, 3, 4, 5])
# view = arr[1:4]
# view[0] = 999
# print(view)
# view[:] = 99
# print(view)
# print(arr)

# copy = arr[1:4].copy()
# copy[0] = 111
# print(arr)
# print('==================================== BOOLEAN AND FANCY INDEXING ====================================')
# a = np.array([10, 15, 20, 25, 30])
# mask = a > 20
# print(mask)
# print(a[mask])
# a[a>20] = 0
# print(a)

# a = np.array([100, 200, 300, 400, 500])
# print(a[1, 3])

print('======================================= HOMEWORK =======================================')