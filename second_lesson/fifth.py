arr = [34.45, 56.4, 67.5, 67, 94.5, 34.1, 3.94, 25.34, 43, 23.4, 53.2, 11.04]
cent = 0
arr.sort()

print(arr)

for i in range(0, len(arr)):
    cent = '00' if round((arr[i] % 1) * 100 // 1) == 0 else round(arr[i] % 1 * 100) # копейки = нулям, если число целое
    if cent != '00' and cent < 10: # добавляем ноль впереди числа, если копеек меньше 10
        cent = '0' + str(cent)
    arr[i] = str(int(arr[i] / 1)) + ' руб ' + cent + ' коп,'

print(*arr)
