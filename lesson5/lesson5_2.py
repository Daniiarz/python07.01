d = {
    'apple': 'яблоко',
    'white': 'белый',
    'red': 'красный',
    'walk': 'ходить',
    'car': ['машина', 'автомобиль'],
    'dictionary': {
        'car': 'машина',
        'white': 'белый',
    },
    'date': ['свидание', 'финик', 'дата', 'встречаться'],
    'zero': 0,
    0: 'Ноль'
}

d_rus = {
    'машина': 'car',
    'автомобиль': 'car',
}

for i in list(d.keys()) + list(d_rus.keys()):
    print(i)


while True:
    lang = input("Выберите язык словаря ")
    if lang == 'en':
        word = input('Слово с анг на русс ')
        try:
            print(d[word])
        except KeyError:
            print("Нету такого слова")
            action = input("Хотите новое слово? ")
            if action == "Y":
                d[word] = input(f'Введите перевод к слову {word} ')
    elif lang == 'ru':
        word = input('Слово с русс на анг ')
        print(d_rus[word])
    else:
        print("Выберите один из языков!")
