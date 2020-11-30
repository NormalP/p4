from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(100, 1000))
num_sum = 0
for i in numbers:
    num_sum += i
print(num_sum)
print(num_sum)