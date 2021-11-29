class NoStr:
    num_list = []

    @staticmethod
    def no_str(num):
        try:
            if int(num) is not str:
                NoStr.num_list.append(num)
        except:
            print(ValueError('Введите число, а не строку'))


el = None
while True:
    el = input('Введите число: ')
    if el == 'stop':
        break
    NoStr.no_str(el)

print(NoStr.num_list)
