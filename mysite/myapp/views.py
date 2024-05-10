from .models import List
from django.shortcuts import render
from django.db.models import Q
from functools import reduce
from django.db.models import F


prof = ['Физик', 'Астроном', 'Политик', 'Писатель', 'Драматург', 'Поэт', 'Изобретатель', 'Музыкант', 'Певец',
               'Художник', 'Ученый', 'Филантроп', 'Президент',
               'Философ', 'Военачальник', 'Актриса',
               'Биолог', 'Космолог', 'Актер', 'Боец', 'Режиссер', 'Сценарист',
               'Продюсер', 'Математик', 'Юморист', 'Экономист',
               ]

country = ['Германия', 'Великобритания', 'Англия', 'Сербия', 'Австрия', 'США', 'Италия', 'Индия', 'Шотландия',
        'Польша', 'Испания', 'Мексика', 'Франция', 'Швеция', 'ЮАР', 'Россия', 'Китай', 'Греция',
        'Рим', 'Аравия', 'Израиль', 'Македония', 'Швейцария',
        'Ирландия']


def index(request):
    data = List.objects.all()

    return render(request, r"myapp\index.html", {'data': data, 'country': country, 'prof': prof})


def search_name(request):
    query_name = request.GET.get('q')
    query_p = request.GET.getlist('prof')
    query_c = request.GET.getlist('country')
    query_d1 = request.GET.get('date1')
    query_d2 = request.GET.get('date2')

    query_res = List.objects.all()

    if query_name:
        query_res = List.objects.filter(Q(name__icontains=query_name))
    if query_p:
        query_res = List.objects.filter(reduce(Q.__or__, [Q(profession__icontains=word) for word in query_p]))
    if query_c:
        query_res = List.objects.filter(reduce(Q.__or__, [Q(country__icontains=word) for word in query_c]))
    if query_d1:
        query_res = List.objects.filter(year1__gte=query_d1)
    if query_d2:
        query_res = List.objects.filter(year2__lte=query_d2)

    return render(request, r"myapp\search_results.html", {"query_res": query_res, 'country': country, 'prof': prof})