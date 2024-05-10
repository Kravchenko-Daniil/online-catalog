import sqlite3
import requests
import wikipedia
import json
import pandas as pd
import re


peoples = ['Эйнштейн, Альберт', 'Уинстон Черчилль', 'Шекспир Уильям', 'Никола Тесла', 'Моцарт Вольфганг Амадей',
           'Майкл Джексон', 'Леонардо да Винчи', 'Адольф Гитлер', 'Махатма Ганди', 'Стив Джобс', 'Билл Гейтс',
           'Александр Грэм Белл', 'Авраам Линкольн', 'Мария Кюри', 'Пабло Пикассо', 'Фрида Кало',
           'Джон Леннон', 'Жаклин Кеннеди', 'Августин, Святой', 'Наполеон Бонапарт', 'Клинтон, Билл',
           'Обама, Барак', 'Мэрилин Монро', 'Альфред Нобель', 'Генри Форд', 'Мадонна', 'Чарльз Дарвин', 'Стивен Хокинг',
           'Чак Норрис', 'Нельсон Мандела', 'Вуди Аллен', 'Квентин Тарантино', 'Джими Хендрикс', 'Брюс Ли',
           'Франклин Рузвельт', 'Путин, Владимир Владимирович', 'Анджелина Джоли', 'Брэд Питт', 'Виктор Гюго',
           'Галилео Галилей',
           'Вольтер', 'Фёдор Достоевский', 'Готье, Антуан Лоран', 'Ницше, Фридрих', 'Марк Твен', 'Чарльз Диккенс',
           'Верди, Джузеппе', 'Чарльз Чаплин', 'Элвис Пресли', 'Анна Франк', 'Вашингтон, Джордж', 'Карл Маркс',
           'Черчилль, Уинстон', 'Ганди, Махатма', 'Дали, Сальвадор', 'Брукс, Мел', 'Фредди Меркьюри', 'Гейтс, Билл',
           'Холмс, Шерлок', 'Шопен, Фредерик', 'Жак-Ив Кусто', 'Кортес, Эрнан', 'Мао Цзэдун', 'Платон', 'Сократ',
           "Жанна д'Арк", 'Цезарь, Юлий', 'Христос', 'Будда', 'Мухаммад', 'Соломон', 'Пифагор', 'Гомер', 'Моисей',
           'Конфуций', 'Александр Великий', 'Юлий Цезарь', 'Пётр Великий', 'Генрих VIII', 'Махомет',
           'Леонардо да Винчи', 'Колумб, Христофор', 'Наполеон I', 'Бах, Иоганн Себастьян', 'Вагнер, Рихард',
           'Майкл Фарадей', 'Людвиг ван Бетховен', 'Толст   ой, Лев', 'Гомер', 'Жан-Жак Руссо',
           'Боклер, Чарльз, 1-й герцог Сент-Олбанс',
           'Уайльд, Оскар', 'Генри Филдинг', 'Георг Вильгельм Фридрих Гегель', 'Сенека', 'Павел Флоренский',
           'Шарль Бодлер', 'Аристотель']

wikipedia.set_lang('ru')

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def create_table():
    cursor.execute('''
        CREATE TABLE Persons (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date1 TEXT,
        date2 TEXT,
        profession TEXT,
        country TEXT,
        photo TEXT,
        wiki TEXT
        )
    ''')


def get_links():    
    WIKI_REQUEST = 'http://ru.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='

    for people in peoples:
        result = wikipedia.search(people, results=1)
        wkpage = wikipedia.WikipediaPage(title=result[0])
        title = wkpage.title
        page = wikipedia.page(title)
        response = requests.get(WIKI_REQUEST + title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']

        cursor.execute('INSERT INTO Persons (name, photo, wiki) VALUES (?, ?, ?)', (people, img_link, page.url))
        connection.commit()


# peoples = peoples[14:]


def get_other():
    file = pd.read_excel('test/e.xlsx')
    data = pd.DataFrame(file)

    # print(data)
    for row in data.values:
        name, date1, date2, prof, country = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip()

        # cursor.execute('UPDATE Persons SET date1 = ? WHERE name = ?', (date1, name))
        # cursor.execute('UPDATE Persons SET date2 = ? WHERE name = ?', (date2, name))
        cursor.execute('UPDATE Persons SET profession = ? WHERE name = ?', (country, name))
        cursor.execute('UPDATE Persons SET country = ? WHERE name = ?', (prof, name))

        print(name, date1, date2, country, prof)

    connection.commit()


if __name__ == "__main__":
    # create_table()
    # get_links()
    # get_other()
    c = 0
    d = cursor.execute("SELECT * FROM Persons")
    for item in d:
        n = item[1]

        d1, d2 = item[2].strip(), item[3].strip()
        y1, y2 = 0, 0

        if 'до' in d1:
            y1 = 0
        if 'примерно' in d1:
            y1 = 0
        if '?' in d1:
            y1=0
        else:
            y1 = int(d1.split('.')[-1])

        if 'до' in d2:
            y2 = 0
        if 'примерно' in d2:
            y2 = 0
        if 'по наши дни' in d2:
            y2 = 9999
            print(d2)
        else:
            y2 = int(d2.split('.')[-1])

        # print(n, '=', y1, y2)

        c += 1

    print(c)

    connection.commit()
    connection.close()
