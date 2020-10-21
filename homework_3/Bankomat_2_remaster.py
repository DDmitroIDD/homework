# банкомат 2
# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры

banknotes = {1: 10, 2: 20, 5: 50, 10: 100, 20: 200}
banknotesBig = [1000, 500, 200, 100, 50]
inquiry = int(input("Введите сумму: "))
payment = {1: ['x', 0], 2: ['x', 0], 5: ['x', 0], 10: ['x', 0], 20: ['x', 0],
           50: ['x', 0], 100: ['x', 0], 200: ['x', 0], 500: ['x', 0], 1000: ['x', 0]}
banknote = 0

while inquiry:
    if inquiry % 10:
        banknotes[1] -= inquiry % 10
        payment[1][1] += inquiry % 10
        inquiry -= payment[1][1]
    elif inquiry % 100:
        for num in banknotes:
            if num == 1:
                continue
            if banknotes[1] == 10:
                inquiry -= banknotes[1]
                banknotes[1] = 0
                payment[1][1] = 10
            if inquiry % 100 - banknotes[num] >= 0:
                payment[num][1] += banknotes[num] // num
                inquiry -= banknotes[num]
                banknotes[num] = 0
            elif banknotes[num] - inquiry % 100 >= 0:
                banknotes[num] -= inquiry % 100
                payment[num][1] += inquiry % 100 // num
                inquiry -= inquiry % 100
    else:
        if banknotes[10] == 100:
            inquiry -= banknotes[10]
            payment[10][1] += banknotes[10] // 10
            banknotes[10] = 0
        elif banknotes[20] == 200:
            inquiry -= banknotes[20]
            payment[20][1] += banknotes[20] // 20
            banknotes[20] = 0

        if banknotesBig[banknote] == inquiry:
            payment[banknotesBig[banknote]][1] += 1
            inquiry -= banknotesBig[banknote]
        elif inquiry - banknotesBig[banknote] >= 0:
            payment[banknotesBig[banknote]][1] += 1
            inquiry -= banknotesBig[banknote]
        elif banknote < len(banknotes)-1:
            banknote += 1
        else:
            banknote = 0
for key, value in payment.items():
    print(key, *value)
