from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def GetData():
    return [
        {'title': 'Заказ №1', 'id': 1,
         'description': 'Латте 0,3; сироп малина; синабон',
         'count': '3 позиции',
         'price': '450 рублей'},

        {'title': 'Заказ №2', 'id': 2,
         'description': 'Эсперессо; Аммерикано 0,4',
         'count': '2 позиция',
         'price': '250 рублей'},

        {'title': 'Заказ №3', 'id': 3,
         'description': 'Фраппе',
         'count': '1 позиция',
         'price': '200 рублей'},

        {'title': 'Заказ №4', 'id': 3,
         'description': 'Сэндвич; Латте 0,3',
         'count': '2 позиции',
         'price': '480 рублей'}
    ]



def hello(request):
    return HttpResponse('Hello world!')

def hello(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'cars': GetData()
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'cars': GetData()

    }})


