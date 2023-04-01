import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=list('ABC'))
print(df)

# a
d_1 = list(map(lambda a, b, c: a + b + c, df['A'], df['B'], df['C']))
print(d_1)

d_2 = [df['A'][i] + df['B'][i] + df['C'][i] for i in range(10)]
print(d_2)

# b
e_1 = list(map(lambda a, b, c: a * a + b * b + c * c, df['A'], df['B'], df['C']))
print(e_1)

e_2 = [df['A'][i] ** 2 + df['B'][i] ** 2 + df['C'][i] ** 2 for i in range(10)]
print(e_2)

# c
f_1 = list(map(lambda x: x if x > 80 else sum(df['B']) / 10, df['A']))
print(f_1)

f_2 = [i if i > 80 else sum(df['B']) / 10 for i in df['A']]
print(f_2)
