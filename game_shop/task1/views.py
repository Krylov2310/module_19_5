from django.shortcuts import render
from .models import Game, Buyer, News
from .forms import UserRegister
from django.core.paginator import Paginator


context = {}


def info(request):
    context = {'base_student': 'Студент: Крылов Эдуард Васильевич',
               'base_title': 'Навигационная страница'
               }
    return render(request, 'info/info.html', context)


def get_menu(request):
    context['base_title'] = 'Магазин игр'
    return render(request, 'fourth_task/menu.html', context)


def games(request):
    # Получаем все посты
    set_games = Game.objects.all()

    # Получаем количество постов на странице из GET-параметров, если оно указано
    per_page = request.GET.get('per_page', 3)  # по умолчанию 5 постов на странице
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 3  # если не число, то ставим значение по умолчанию

    # Настроим пагинацию
    paginator = Paginator(set_games, per_page)

    # Получаем номер текущей страницы из запроса
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Передаем данные в шаблон
    return render(request, 'fourth_task/games.html', {'page_obj': page_obj, 'per_page': per_page})


def cart(request):
    context['base_title'] = 'Корзина'
    return render(request, 'fourth_task/cart.html', context)


def sign_by_django(request):
    context = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            set_user = Buyer.objects.values_list('name', flat=True)

            if username in set_user:
                context['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                context['error'] = 'Пароли не совпадают'
            elif age <= 17:
                context['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                context['message'] = f'Пользователь, {username} успешно зарегистрирован!'

    context['form'] = form

    return render(request, 'fifth_task/registration_page.html', context)


def news_list(request):
    # Получаем все посты
    news = News.objects.all().order_by('-date')

    # Получаем количество постов на странице из GET-параметров, если оно указано
    per_page = request.GET.get('per_page', 3)  # по умолчанию 3 поста на странице
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 3  # если не число, то ставим значение по умолчанию

    # Настроим пагинацию
    paginator = Paginator(news, per_page)

    # Получаем номер текущей страницы из запроса
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Передаем данные в шаблон
    return render(request, 'six_task/news.html', {'page_obj': page_obj, 'per_page': per_page})
