# практика 1
# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

from names import get_full_name
from random import sample
from random import randint

students = {'Smirnov Semen': [45, 67, 35, 79], 'Ivanov Ivan': [54, 23, 87, 95],
            'Dmytriev Dmytro': [36, 74, 89, 22], 'Petrov Petr': [90, 87, 66, 99]}
average_scores = {}
for i in students:
    average_scores.setdefault(i, sum(students[i]) / len(students[i]))
print(*max(average_scores.items()), *min(average_scores.items()))

# практика 2
# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:

# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java


programmers = {}
number_of_students = 12
groups = ['Python', 'FrontEnd', 'FullStack', 'Java']
for i in range(number_of_students):
    programmers.setdefault(get_full_name(), sample(groups, k=randint(1, 4)))
print('\n' + 'Студенты, которые учатся в двух и более группах' + '\n')

for j in programmers:
    if len(programmers[j]) > 1:
        print(j + ' => ', *programmers[j])

print('\n' + 'Студенты, которые не учатся на фронтенде' + '\n')

for x in programmers:
    if 'FrontEnd' not in programmers[x]:
        print(x + ' => ', *programmers[x])

print('\n' + 'Студенты, которые изучают Python или Java' + '\n')

for y in programmers:
    if ('Java' or 'Python') in programmers[y]:
        print(y + ' => ', *programmers[y])



