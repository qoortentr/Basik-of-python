from time import perf_counter
import sys


def num_gen(gen_list):
    for i in range(len(gen_list) - 1):
        if gen_list[i] < gen_list[i + 1]:
            yield gen_list[i + 1]


def num_lists(list_list):  # список для сравнения по скорости и объему памяти
    add = []
    for i in range(len(list_list) - 1):
        if list_list[i] < list_list[i + 1]:
            add.append(list_list[i + 1])
    return add


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

num_list = num_gen(src)
print(*num_list)
#  проверка на расход памяти и скорость работы
# start = perf_counter()
# print(perf_counter() - start, '- время работы спискa.', sys.getsizeof(num_list), '- размер.', type(num_list), '- тип')
#
# start = perf_counter()
# size_list = num_lists(src)
# print(perf_counter() - start, '- время работы списка.', sys.getsizeof(size_list), ' - размер.', type(size_list),
#       '- тип')
