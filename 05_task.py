import os

dict_files = {100: 0, 1000: 0, 10000: 0, 100000: 0}
file = 'some_data'
extension = set()  # множество для расширений

num = 0  # счетчики для изменения значений внутри словарей
numa = 0
numb = 0
numc = 0

for name in os.listdir('some_data'):

    file_path = os.path.join(file,  name)  # конкатенация пути
    file_extension = file_path.split('.')[-1]  # расширение файла

    if os.stat(file_path).st_size <= 100:
        num += 1
        extension.add(file_extension)
        add = (num, [file_extension])
        dict_files[100] = add
    elif os.stat(file_path).st_size <= 1000:
        numa += 1
        extension.add(file_extension)
        add = (numa, [file_extension])
        dict_files[1000] = add
    elif os.stat(file_path).st_size <= 10000:
        numb += 1
        extension.add(file_extension)
        add = (numb, [file_extension])
        dict_files[10000] = add
    else:
        numc += 1
        extension.add(file_extension)
        add = (numc, [file_extension])
        dict_files[100000] = add

with open('hw7_summary.json', 'w', encoding='utf-8') as f:  # запись словаря в файл
    f.write(str(dict_files))

print(dict_files)
