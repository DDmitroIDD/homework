from random import randint

# Банкомат 1
# Банкомат выдает сумму максимально возможными купюрами

banknotes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
payment = []
inquiry = int(input("Введите сумму: "))
banknote = 0
while inquiry != sum(payment):
    if banknotes[banknote] == inquiry:
        payment.append(banknotes[banknote])
    elif banknotes[banknote] + sum(payment) <= inquiry:
        payment.append(banknotes[banknote])
    elif banknote < len(banknotes)-1:
        banknote += 1
    else:
        banknote = 0
print(*payment)


# fizzbuzz prt.1 and prt.2
# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

with open('fizzbuzz30.txt', 'w') as fizzbuzz:
    for i in range(30):
        a = [str(randint(2, 50)) for j in range(3)]
        fizzbuzz.write(' '.join(a) + '\n')

with open('fizzbuzz30Ans.txt', 'w') as fizzbuzzAns:
    with open('fizzbuzz30.txt') as buzzfizz:
        for line in buzzfizz:
            fizz, buzz, third = line.split(' ')
            fizz, buzz, third = int(fizz), int(buzz), int(third)
            num = []

            for i in range(1, third+1):
                if not i % fizz and not i % buzz:
                    num.append('FB')
                elif not i % fizz:
                    num.append('F')
                elif not i % buzz:
                    num.append('B')
                else:
                    num.append(str(i))
            print(*num)

            # Переделать вторую задачу так, чтобы результат писался в другой файл

            fizzbuzzAns.write(' '.join(num) + '\n')
