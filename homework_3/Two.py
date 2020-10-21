# практика 1
# Каждый пишет сумму списка при помощи for и while

mas = [1, 2, 3, 4, 5, 6]
summa = 0

for i in mas:
    summa += i
print(summa)

summa = 0
ind = 0

lenn = len(mas)
while ind < lenn:
    summa += mas[ind]
    ind += 1
print(summa)

# практика 2
# Написать программу, которая выводит сама себя

with open('Two.py', 'r') as test:
    for i in test:
        print(i, end='')

# практика 2
# Написать программу, которая выводит саму себя задом наперед

rev = []
with open('Two.py', 'r') as test:
    for i in test:
        rev.append(i)
print(*rev[::-1])
