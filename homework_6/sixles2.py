# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внтри функции нужно просто обращаться к правильно составленному словарю.

def sizer(size, country):
    countries = {
    'Russia': {'xxs': 42, 'xs': 44, 's': 46, 'm': 48, 'l': 50, 'xl': 52, 'xxl': 54, '3xl': 56},
    'Germany': {'xxs': 36, 'xs': 38, 's': 40, 'm': 42, 'l': 44, 'xl': 46, 'xxl': 48, '3xl': 50},
    'USA': {'xxs': 8, 'xs': 10, 's': 12, 'm': 14, 'l': 16, 'xl': 18, 'xxl': 20, '3xl': 22},
    'France': {'xxs': 38, 'xs': 40, 's': 42, 'm': 44, 'l': 46, 'xl': 48, 'xxl': 50, '3xl': 52},
    'United Kingdom': {'xxs': 24, 'xs': 26, 's': 28, 'm': 30, 'l': 32, 'xl': 34, 'xxl': 36, '3xl': 38}
    }
    return print('Ваш размер: ' + str(countries[country][size]))


siz = input('Введите размер: xxs, xs, s, m, l, xl, xxl or 3xl : ')
coun = input('Введите страну: Russia, Germany, USA, France or United Kingdom : ')
sizer(siz, coun)
