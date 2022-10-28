from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def ful_sum(n):
    time_0 = datetime.now()
    k = 0
    for i in range(n + 1):
        if '0' not in str(i):
            s = sum(int(x) for x in str(i)) - str(i).count('1')
            flag = not ((s == 5) and ('5' in str(i)))
            if (s >= 5) and flag:
                k += 1
    # print('Колличество_0 = ', k)
    total_0 = datetime.now() - time_0
    # print('Время при нахождении суммы через sum: ', total_0.total_seconds())
    return total_0.total_seconds()


def ful_sum_list(n):
    time_1 = datetime.now()
    k = 0
    for i in range(n + 1):
        if '0' not in str(i):
            a = list(map(int, list(str(i))))
            s = sum(a) - a.count(1)
            flag = not ((s == 5) and (5 in a))
            if (s >= 5) and flag:
                k += 1
    # print('Колличество_1 = ', k)
    total_1 = datetime.now() - time_1
    # print('Время при нахождении суммы через sum с доп списком: ', total_1.total_seconds())
    return total_1.total_seconds()


def sum_before_5(n):
    time_2 = datetime.now()
    k = 0
    for i in range(n + 1):
        s = 0
        if '0' not in str(i):
            for j in str(i):
                s += int(j) if j != '1' else 0
                flag = not ((s == 5) and ('5' in str(i)))
                if s >= 5 and flag:
                    k += 1
                    break
    # print('Колличество_2 = ', k)
    total_2 = datetime.now() - time_2
    # print('Время при нахождении суммы до 5: ', total_2.total_seconds())
    return total_2.total_seconds()


def multiply_before_5(n):
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
    # print('Колличество_3 = ', k)
    total_3 = datetime.now() - time_3
    # print('Время при перемножении до 5: ', total_3.total_seconds())
    return total_3.total_seconds()


def ful_multiply(n):
    time_4 = datetime.now()
    k = 0
    for i in range(n + 1):
        m = 1
        for j in str(i):
            m *= int(j)
        if m > 5:
            k += 1
    # print('Колличество_4 = ', k)
    total_4 = datetime.now() - time_4
    # print('Время при полном перемножении: ', total_4.total_seconds())
    return total_4.total_seconds()


if __name__ == '__main__':
    n = 10000000
    n_list = list(range(1, n + 2, 100000))
    # ful_sum_lst = [ful_sum(x) for x in n_list]
    # print('Расчитали массив: при нахождении суммы через sum')

    # ful_sum_list_lst = [ful_sum_list(x) for x in n_list]
    # print('Расчитали массив: при нахождении суммы через sum с доп списком')

    sum_before_5_lst = [sum_before_5(x) for x in n_list]
    print('Расчитали массив: при нахождении суммы до 5')

    multiply_before_5_lst = [multiply_before_5(x) for x in n_list]
    print('Расчитали массив: при перемножении до 5')

    # ful_multiply_lst = [ful_multiply(x) for x in n_list]
    # print('Расчитали массив: при полном перемножении')

    plt.figure()
    # plt.plot(n_list, ful_sum_lst)
    # plt.plot(n_list, ful_sum_list_lst)
    plt.plot([i//100000 for i in n_list], sum_before_5_lst)
    plt.plot([i//100000 for i in n_list], multiply_before_5_lst)
    # plt.plot(n_list, ful_multiply_lst)
    # plt.xticks(rotation=90)
    plt.xlabel('N/100000')
    plt.ylabel('Time')
    plt.legend(['при нахождении суммы до 5', 'при перемножении до 5'])
    plt.show()
