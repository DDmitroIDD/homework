from random import randint
# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!

def fbt(f, b, t, n):
    for i in range(1, t + 1):
        if not i % f and not i % b:
            n.append('FB')
        elif not i % f:
            n.append('F')
        elif not i % b:
            n.append('B')
        else:
            n.append(str(i))
    return n


with open('fizzbuzz30.txt', 'w') as fizzbuzz:
    for _ in range(30):
        a = [str(randint(2, 50)) for j in range(3)]
        fizzbuzz.write(' '.join(a) + '\n')

with open('fizzbuzz30Ans.txt', 'w') as fizzbuzzAns:
    with open('fizzbuzz30.txt') as buzzfizz:
        for line in buzzfizz:
            fizz, buzz, third = map(int, line.split(' '))
            num = []
            fbt(fizz, buzz, third, num)
            print(*num)

            fizzbuzzAns.write(' '.join(num) + '\n')
