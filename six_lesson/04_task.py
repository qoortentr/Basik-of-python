from itertools import zip_longest

with open('str.txt', 'w', encoding='utf-8') as fs:
    with open('hobby.csv', 'r', encoding='utf-8') as fh:
        with open('users.csv', 'r', encoding='utf-8') as fu:
            dict_info = {}

            gen_hobby = (line.split(',') for line in fh)  # генератор хобби

            gen_name = (line.split(',') for line in fu)  # генератор имен

            for i, p in zip_longest(gen_name, gen_hobby, fillvalue='None'):  # коррекция вида строк и запись в словарь
                if i == 'None':  # если пользователей больше чем хобби
                    exit(1)
                i = ' '.join(i).replace('\n', '')
                if p != 'None':  # если у пользователя нет хобби
                    p = ', '.join(p).replace('\n', '')
                fs.write(i + ': ' + p + '\n')  # запись текста в файл
