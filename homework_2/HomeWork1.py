# Задание 1
# Пример 1
# Проверить, является ли введеное число четным.


number = int(input('Введите число '))
if not number % 2:
    print('You entered an even number')
else:
    print('You entered an odd number')

# Пример 2
# Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.

number = int(input('Введите число '))

if number % 2 and number // 3 and number // 5 and not number // 10:
    print('Yes')
else:
    print('No')


# Пример 3
# Ввести число, вывести все его делители.

number = int(input('Введите число '))

for i in range(1, number+1):
    if not number % i:
        print(i)


# Практика 4
# Ввести число, вывести его разряды и их множители.

number = input('Введите число ')

dis = []
discharge = int(len(number))
for i in number:
    i = int(i)
    for j in range(discharge-1):
        i *= 10
    discharge -= 1
    if i:
        dis.append(i)
print(*dis)


number = int(number)
div = 2
mult = []

while div * div <= number:
    if number % div == 0:
        mult.append(div)
        number //= div
    else:
        div += 1
if number > 1:
    mult.append(number)
print(*mult)


# Задание 2
# Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.

a = int(input('Введите число '))
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')



# Задание 3
# fizzbuzz


fizz, buzz, third = int(input('Введите число ')), int(input('Введите число ')), int(input('Введите число '))
num = []

for i in range(1, third+1):
    if not i % fizz and not i % buzz:
        num.append('FB')
    elif not i % fizz:
        num.append('F')
    elif not i % buzz:
        num.append('B')
    else:
        num.append(i)
print(*num)