from django.shortcuts import render, HttpResponse
from django.template.defaultfilters import random

from task1.forms import UserRegister
from task1.models import Buyer, Game

# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    games_all = Game.objects.all()
    cost = 'Стоимость:'
    context = {'games': games_all, 'cost': cost}
    return render(request, "fourth_task/games.html", context)


def cart(request):
    return render(request, "fourth_task/cart.html")


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.Post)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']
        if password == repeat_password and age >= 18 and Buyer.objects.filter(username=username).exists() == False:
            Buyer.name = username
            Buyer.age = age
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if age < 18:
            info['error'] = 'Вы должны быть старше 18!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if Buyer.objects.filter(username=username).exists():
            info['error'] = 'Такое имя уже существует'
            return render(request, 'fifth_task/registration_page.html')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and Buyer.objects.filter(username=username).exists() == False:
            Buyer.objects.create(username=username, age=age, balance=2000)
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if Buyer.objects.filter(username=username).exists():
            info['error'] = 'Такое имя уже существует'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
    return render(request, 'fifth_task/registration_page.html')
