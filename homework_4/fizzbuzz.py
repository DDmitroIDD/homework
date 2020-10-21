from random import randint

# Заканчиваем прошлые задачи,
# украшаем работу физбазов работой со строками, списками, пробуем генераторы списков и прочие новые красоты,
# которые выучили. Доводим код до идеала!
#

with open('fizzbuzz30.txt', 'w') as fizzbuzz:
    for i in range(30):
        a = [str(randint(2, 50)) for j in range(3)]
        fizzbuzz.write(' '.join(a) + '\n')

with open('fizzbuzz30Ans.txt', 'w') as fizzbuzzAns:
    with open('fizzbuzz30.txt') as buzzfizz:
        for line in buzzfizz:
            fizz, buzz, third = map(int, line.split(' '))
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

            fizzbuzzAns.write(' '.join(num) + '\n')
