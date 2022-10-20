# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# НОД (99, 54) = 9, НОК (99, 54) = 594.
# Число, на которое оба делятся без остатка
# найти макс, потом перебрать от мах до ... проверить, что оно делится на оба


try:
    print("Поиск наименьшего общего кратного")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    if a > b:
        max_num = a
    else:
        max_num = b

    for n in range(max_num, 0, -1):
        if (a % n == 0) and (b % n == 0):
            print(n)
            break

except:
    print("Введены некоректные данные!")
