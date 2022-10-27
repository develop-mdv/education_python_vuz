"""Вводится вектор. Вывести максимум из его элементов."""
a = list(map(int, input().split()))
print(max(a))

"""	Данные об email-адресах студентов хранятся в словаре: {домен:логины} .
 Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен"""
s = input()[1:-1]
email_dict = {}
while s.find(':') != -1:
    key_end = s.find(':')
    key = s[0:key_end]
    value_end = s.find(']')
    value = s[key_end+3: value_end].split(', ')
    email_dict[key] = value
    s = s[value_end+3:]
email_list = []
for key, value in email_dict.items():
    for name in value:
        email_list.append(name+'@'+key)
email_list.sort()
print(*email_list, sep='\n')

"""	Напишите программу, которая помогает определить какие вещи могут поместиться в рюкзак.
Вводится существующий объем рюкзака. Затем вводятся объемы всех вещей, которые хочется туда поместить.
 Нужно вывести список объемов вещей, которые поместятся в рюкзак.
 Постарайтесь максимизировать кол-во вошедших вещей."""
volume = int(input())
items = list(map(int, input().split()))
volume_sum = []

for i in items:
    if sum(volume_sum) + i < volume:
        volume_sum.append(i)
    else:
        break
print(*volume_sum)

"""Вводится вектор. Заменить в нём каждое число Фибоначчи на следующее."""
a = list(map(int, input().split()))
fib_max = max(a)
fib_list = [1, 1]
while fib_list[-1] < fib_max:
    fib_list.append(fib_list[-1]+fib_list[-2])

for i in range(len(a)):
    if a[i] in fib_list:
        a[i] = fib_list[fib_list.index(a[i])+1]
print(*a)
