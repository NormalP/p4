from itertools import cycle
from random import randint
с = 0
a = int(input())
for el in cycle("фвфы"):
    if с > 10:
        break
    print(randint(a, (a+1000000)))
    с += 1
some_num = ["1", "2", "3", "4"]
iter = cycle(some_num)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))