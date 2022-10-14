"""	На вход подается строка, состоящая из одного числа. Напишите программу, которая удваивает его. """
a = int(input())
print(2*a)

"""Вводится число. Вывести его квадрат."""
a = int(input())
print(a**2)

"""Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
Вывести, какая часть суток прошла (число от 0 до 1)."""
hour = int(input().split()[1])
minute = int(input().split()[1])
seconds = int(input().split()[1])
seconds_from_midnight = hour*3600 + minute*60 + seconds
day_part = seconds_from_midnight/24*3600
print(f'seconds:{seconds_from_midnight}')
print(f'day part:{day_part}')

"""Вводится число. Вывести, оканчивается ли оно на цифру 7, не используя приведение к строке и операции над строками"""
a = int(input())
if a % 10 == 7:
    print('TRUE')
else:
    print('FALSE')

"""Вводятся коэффициенты уравнения ax2+bx+c=0. Вывести его корни(не забыть проверить, что a не равно 0)"""
f = input()
if f.find('x2') == -1 or int(f[:f.find('x2')]) == 0:
    print('ERROR: a == 0')
else:
    a = int(f[:f.find('x2')])
    b = int(f[f.find('x2')+2:f.rfind('x')])
    c = int(f[f.rfind('x')+1:f.rfind('=')])
    import numpy
    print(*numpy.roots((a, b, c)))

"""Вводятся три числа. Вывести максимум из них."""
print(max(list(map(int, input().split()))))

"""Вводится число. Вывести среднее арифметическое (с точностью до двух знаков после запятой) 
тех чисел в диапазоне от единицы до введённого числа, которые делятся 5 или являются четными."""
a = int(input())
even = (1 + a//2)*(a//2)
five = (5 + a//5*5)*(a//5) / 2
average = (even + five)/(a//2 + a//2)
print(average)
