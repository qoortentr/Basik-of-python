import random


def get_jokes(num):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    while num != 0:
        joke = nouns[(random.randint(0, 4))] + " " + adverbs[(random.randint(0, 4))] + " " + adjectives[
            (random.randint(0, 4))]
        jokes_list.append(joke)
        num -= 1
    print(jokes_list)


jokes = int(input('Введите количество шуток: '))

get_jokes(jokes)
