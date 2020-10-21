# prt.1
#Задача 1. Курьер

# Вам известен номер квартиры, этажность дома и количество квартир на этаже.
# Задача: написать функцию, которая по заданным параметрам напишет вам,
# в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.


import math

number = int(input('введите № квартиры: '))
floor = int(input("введите этажность: "))
apart_on_the_floor = int(input("введите колличество квартир на этаже: "))
entrance = 1
apart_in_entrance = floor * apart_on_the_floor

while number > apart_in_entrance:
    number -= apart_in_entrance
    entrance += 1

number /= apart_on_the_floor

print('Этаж ' + str(math.ceil(number)) + ' Подъезд ' + str(entrance))

# prt.2
# Задача 2. Бриллиант
#
# Входным данным является целое число. Необходимо:
#
# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли.
# Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда, потом три звезды, потом опять одна,
# для пятерки - звезда, три, пять, три, одна...

number = int(input('Введите число: '))
while number <= 0:
    number = int(input('Введите положительное число: '))

numbers = [i for i in range(1, number if not number % 2 else number + 1, 2)]
ran = [x for x in range(len(numbers)-1, -1, -1)]

numbers.extend(numbers[-2::-1])
ran.extend(ran[-2::-1])

brilliant = list(map(lambda x, y: print(x * ' ' + y * '*'), ran, numbers))


# prt.3

# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:
#
# 2 4 5;3 2
# 3 2 1;2 0
# 6 5 2 1 2;3 1
# .....
# Цифры до точки с запятой надо суммировать, потом делить на их количество.
# В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2.
# Аналогичным образом во второй строке 6 делим на три, ровно два и в сотатке ноль,
# в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке. Вот так:
#
# 2 4 5;3 2                 2+4+5/3 = 3, в остатке 1
# 3 2 1;2 0                 3+2+1/3 = 2, в остатке 0
# 6 5 2 1 2;3 1         6+5+2+1+2/5 = 3, в остатке 1
# .....
# Задача: проверить каждую строку файла, если строка записана верно,
# вывести ее и после написать True, если строка не верна, вывести результат с пометкой False.


def aver_num1(num1):
    c = sum(map(int, num1.strip('\n').split(';')[0].split())) // len(num1.strip('\n').split(';')[0].split())
    d = sum(map(int, num1.strip('\n').split(';')[0].split())) % len(num1.strip('\n').split(';')[0].split())
    return str(c) + '.' + str(d)


def aver_num2(num2):
    return '.'.join(num2.strip('\n').split(';')[1].split())


with open('average.txt') as num:
    for numbers in num.readlines():
        if aver_num1(numbers) == aver_num2(numbers):
            print(numbers.strip('\n'), end=' True\n')
        else:
            print(numbers.strip('\n'), end=' False\n')
