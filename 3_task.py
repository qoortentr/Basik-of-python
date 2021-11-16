def tuple_gen(list_1, list_2):
    k = len(list_1) - len(list_2)
    if k > 0:
        for _ in range(k):
            list_2.append('None')
    for t, k in zip(list_1, list_2):
        yield (t, k)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = tuple_gen(tutors, klasses)
print(*gen)
