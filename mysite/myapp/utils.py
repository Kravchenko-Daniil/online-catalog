from .models import List
import sqlite3


con = sqlite3.connect(r'D:\proj\diplom\Diplom\database.db')
cursor = con.cursor()
data = cursor.execute("SELECT * FROM Persons")


def create_data():
    for item in data:
        entry = List.objects.create(name=item[1], date1=item[2], date2=item[3], profession=item[4], country=item[5], photo=item[6], wiki=item[7])
        entry.save()


def update_years():
    for item in data:
        d1, d2 = item[2].strip(), item[3].strip()
        y1, y2 = 0, 0

        if 'до' in d1:
            y1 = 0
        elif 'примерно' in d1:
            y1 = 0
        elif '?' in d1:
            y1 = 0
        elif d1 == '' or d1 == ' ':
            y1=0
        else:
            y1 = d1.split('.')[-1]

        if 'до' in d2:
            y2 = 0
        elif 'примерно' in d2:
            y2 = 0
        elif 'дни' in d2:
            y2 = 9999
        elif d2 == '' or d2 == ' ':
            y2=0
        else:
            y2 = d2.split('.')[-1]

        na = item[1]

        # e = List.objects.get(name=na)
        # e.year1 = y1
        # e.year2 = y2
        # e.save(update_fields=["year1", "year2"])

        List.objects.filter(name=na).update(year1=y1, year2=y2)
