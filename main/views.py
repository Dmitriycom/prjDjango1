from django.shortcuts import render
from django.http import HttpResponse
from soupsieve import match


ttable = [['Інформатика', 'Фізкультура', 'Література', 'Українська мова'],
['Інформатика', 'Математика', 'Література', 'Географія'],
['Фізкультура', 'Математика', 'Математика', 'Українська мова'],
['Математика', 'Інформатика', 'Література', 'Біологія'],
['Література', 'Математика', 'Інформатика', 'Фізкультура']]


def index(request, day):
    response = None
    if day in {'monday', '1', 'Monday'}:
        response = '<h1> Понеділок </h1> <br>'
        for a in ttable[0]: response = response + f'{ttable[0].index(a)+1}. ' + a + '<br>'
    elif day in {'tuesday', '2', 'Tuesday'}:
        response = '<h1> Вівторок </h1> <br>'
        for a in ttable[1]: response = response + f'{ttable[1].index(a)+1}. ' + a + '<br>'
    elif day in {'wednesday', '3', 'Wednesday'}:
        response = '<h1> Середа </h1> <br>'
        for a in ttable[2]: response = response + f'{ttable[2].index(a)+1}. ' + a + '<br>'
    elif day in {'thursday', '4', 'Thursday'}:
        response = '<h1> Четвер </h1> <br>'
        for a in ttable[3]: response = response + f'{ttable[3].index(a)+1}. ' + a + '<br>'
    elif day in {'friday', '5', 'Friday'}:
        response = '<h1> П\'ятниця </h1> <br>'
        for a in ttable[4]: response = response + f'{ttable[4].index(a)+1}. ' + a + '<br>'
    else:
       response = '<h1> Неділля </h1> <br> Вихідий'
    return HttpResponse(response)