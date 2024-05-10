import re

with open('names.txt', 'r', encoding='utf8') as file:
    text = file.readlines()
    res = []

    for i in text:
        # i.replace('\\n', '')
        res.append(i.rstrip())

    print(res)


