# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!


with open('English book.txt') as book:

    letter = list(map(lambda x: x.strip('“!?().,”'), book.read().lower().split()))
    let = dict(zip(letter, map(lambda x: letter.count(x), letter)))
    print(*sorted(let.items(), key=lambda x: x[1], reverse=True))
