from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def login_view(request:HttpRequest) -> HttpResponse:
    print(request.path)
    print(request.method)


    return HttpResponse("Login page")

def orders_view(request:HttpRequest) -> HttpResponse:
    query_params = request.GET

    min_value = query_params.get('min')
    max_value = query_params.get('max')


    return HttpResponse(f"Orders page: [{min_value}, {max_value}]")

def calculators_view(request:HttpRequest) -> HttpResponse:

    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    operator = request.GET.get('op')
   
    if operator == 'add':
        result = num1 + num2
        operator = '+'
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return HttpResponse("0 ga bo'linmaydi")
        result = num1 / num2
    else:
        return HttpResponse("Bunaqa operator mumkin emas")

    return HttpResponse(f"Result: {num1} {operator} {num2} = {result}")

def home_page(r):
    response = render(request=r,template_name='home.html')
    return response