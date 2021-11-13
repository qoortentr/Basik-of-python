dict_ip = {}
# list_data = []  # для задания 1

with open('ip.txt', 'r', encoding='utf-8') as file_1:

    gen_ip = (line.split(' ')[0] for line in file_1)  # извлек ip адреса

    # gen_type = (line.split('/down')[0].split('"')[1] for line in file_1)  #  для задания 1
    # gen_resource = (line.split(' HTTP')[0].split('GET ')[-1] for line in file_1)  #  для задания 1
    #
    # for i in zip(gen_ip, gen_type, gen_resource):  # создаем кортежи из генераторов и помещаем в список
    #     list_data.append(i)                        # для задания 1
    # print(list_data)

    for i in gen_ip:
        if i in dict_ip:
            dict_ip[f'{i}'] += 1
        else:
            dict_ip[f'{i}'] = 1

    max_value = max(dict_ip.values())  # нашел максимальное количество запросов
    ip = list(dict_ip.keys())  # добавил ip в список
    values = list(dict_ip.values())  # добавил количество запросов в список
    index_max = values.index(max_value)  # нашел индекс запроса спамера, а по нему нашел его ip далее
    print('Ip спамера - ' + f'{ip[index_max]}' + '. Количество его запросов - ' + f'{max_value}')
