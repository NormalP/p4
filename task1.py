def my_func():
    x = float(input('количество отработанных часов : '))
    y = float(input('cумма оплаты труда за 1 час : '))
    c = float(input('размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы: {my_func() }')
