from datetime import datetime

n = int(input())
time_3 = datetime.now()
k = 0
for i in range(n + 1):
    if '0' not in str(i):
        m = 1
        for j in str(i):
            m *= int(j)
            if m > 5:
                k += 1
                break
print('Колличество_3 = ', k)
total_3 = datetime.now() - time_3
print('Время при перемножении до 5: ', total_3.total_seconds())
