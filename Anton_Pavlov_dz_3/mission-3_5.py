import random


def jokes(list_1, list_2, list_3):
    random.shuffle(list_1)
    random.shuffle(list_2)
    random.shuffle(list_3)
    joke = zip(list_1, list_2, list_3)
    for i in joke:
        x = list(i)
        print(' '.join(x))


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes(nouns, adverbs, adjectives)
