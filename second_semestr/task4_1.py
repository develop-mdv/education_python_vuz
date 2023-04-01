from random import randint

# Задание 4
# №1
matrix = [[randint(1, 100) for i in range(5)] for k in range(5)]
print(matrix)
# Пункт а.1
less_matrix_1 = list(map(lambda x: list(map(lambda y: y * 0.7, x)), matrix))
print(less_matrix_1)

# Пункт а.2
less_matrix_2 = [[j * 0.7 for j in i] for i in matrix]
print(less_matrix_2)

# Пункт б.1
result_1 = list(filter(lambda x: True if sum(x) < 200 else False, matrix))
print(result_1)

# Пункт б.2
result_1 = [i for i in matrix if sum(i) < 200]
print(result_1)
