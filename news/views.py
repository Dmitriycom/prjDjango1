import imp
from django.shortcuts import render
from django.http import HttpResponse


news_list = {
    "2022":
                {"10":
                    {
                    "20":
                        ["Кабмін призначив Капінуса на посаду голови Пенсійного фонду",
                        "Фонд держмайна виставив на продаж спиртзавод за 31 мільйон",
                        "На Гаванському мосту у Києві загорівся автомобіль"],

                    "21":
                        ["Сьогодні увесь світ відзначає Міжнародний день рідної мови",
                        "У Київській ОДА хочуть зупинити ремонт онкодиспансеру."]
                    },
                "11":
                    {
                    "30":
                        ["Створено першу в історії молекулу-транзистор",
                        "Компанія Renault у 2022 році готує новинки"],
                    "27":
                        ["Створено першу в історії молекулу-транзистор",
                        "Компанія Renault у 2022 році готує новинки"],
                    "31":
                        ["Створено першу в історії молекулу-транзистор",
                        "Компанія Renault у 2022 році готує новинки"]
                    }
                },
            "2021":
                {"5":
                    {
                    "17":
                        ["Як знизити цукор у крові: найкращі ягоди при діабеті 2-го типу",
                        "Україна звернулась до Радбезу ООН щодо гарантування безпеки"]
                    }
                }
            }

def news(request, year=False, month=False, day=False):
    resp = ''
    if(year and month and day and request.GET.get('id')):
        try:
            id = int(request.GET.get('id', 0)) - 1 
            resp = f'{day}.{month}.{year}' + '<br><br> <li>'   + news_list[year][month][day][id] + '</li>'
        except:
            resp ='Неверный год, месяц, день или номер!'
        return HttpResponse(resp)
    elif(year and month and day):
        try:
            resp = f'{day}.{month}.{year}' + '<br><br>'
            for value in news_list[year][month][day]: resp = resp +  '<li>'   + value + '</li>'
        except:
            resp ='Неверный год, месяц или день!'
        return HttpResponse(resp)
    elif(year and month):
        try:
            for value in news_list[year][month]: 
                resp = resp + f'{value}.{month}.{year}' + '<br><br>'
                for item in news_list[year][month][value]:
                    resp = resp +  '<li>'   + item + '</li>'
                resp = resp + '<br><br>'
        except:
            resp = 'Неверный год или месяц!'
        return HttpResponse(resp)
    elif(year):
        try:
            for month in news_list[year]: 
                for day in news_list[year][month]: 
                    resp = resp + f'{day}.{month}.{year}' + '<br><br>'
                    for item in news_list[year][month][day]:
                        resp = resp +  '<li>'   + item + '</li>'
                    resp = resp + '<br><br>'
        except:
            resp = 'Неверный год!'
        return HttpResponse(resp)
    else: 
        for year in news_list: 
            for month in news_list[year]: 
                for day in news_list[year][month]: 
                    resp = resp + f'{day}.{month}.{year}' + '<br><br>'
                    for item in news_list[year][month][day]:
                        resp = resp +  '<li>'   + item + '</li>'
                    resp = resp + '<br><br>'
        return HttpResponse(resp)
