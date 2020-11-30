def fact(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
        yield temp


n = int(input("input num\n"))
for i in fact(n):
    print(i)