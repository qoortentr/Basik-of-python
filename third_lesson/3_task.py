def thesaurus(names_list):
    name_letter = set(map(lambda x: x[:1], names_list))  # берем первые буквы имен без повторов и создаем список из них
    name_list = []  # список для добавления имен
    dict_letter = {}  # словарь для добавления имен и значений
    for i in name_letter:
        for p in range(0, len(names_list)):
            if i == names_list[p][0]:  # если имя начинается на {i}, то добавляем его в список
                name_list.append(names_list[p])
        dict_letter[f"{i}"] = name_list[:]  # присваиваем значение словарю, копия списка
        name_list.clear()  # для очистки прошлых имен
    print(dict_letter)


name = ['Иван', 'Мария', 'Петр', 'Илья']
thesaurus(name)
