numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
squared_odd_numbers = []
total = 0

# Фильтрация нечетных значений 1
odd_numbers_1 = list(filter(lambda x: True if x % 2 == 1 else False, numbers))
print(odd_numbers_1)

# Фильтрация нечетных значений 2
odd_numbers_2 = [i for i in numbers if i % 2 == 1]
print(odd_numbers_2)

# Возведение в квадрат всех нечетных значений 1
squared_odd_numbers_1 = list(map(lambda x: x*x, odd_numbers_2))
print(squared_odd_numbers_1)

# Возведение в квадрат всех нечетных значений 2
squared_odd_numbers_2 = [i*i for i in odd_numbers_2]
print(squared_odd_numbers_2)
