def num_translate_adv(num, numbers):
    if num in numbers:
        print(numbers[num])
    elif num[0].lower() + num[1:] in numbers:
        num = numbers[num.lower()]
        print(num[0].upper() + num[1:])
    else:
        print(None)


numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'}
num = input('Введите число: ')

num_translate_adv(num, numbers)
