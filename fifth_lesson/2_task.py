number = int(input('Введите границу диапазона: '))
num_gen = (i for i in range(1, number + 1, 2))
for j in num_gen:
    print(j)