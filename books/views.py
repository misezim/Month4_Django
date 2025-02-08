from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from . import models

def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html',
                      context=context_object_name)

def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id': query,
        }
        return render(request,
                      template_name='book_detail.html',
                      context=context_object_name)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Добро пожаловать в онлайн-библиотеку!<h1>'
                            ' Здесь вы найдете широкий выбор книг, статей,'
                            'журналов и других материалов для учебы, работы и отдыха. Все ресурсы доступны 24/7, '
                            'и вы можете легко искать нужную информацию через наш удобный каталог. '
                            'Если возникнут вопросы, наша служба поддержки всегда готова помочь. Приятного использования!')

def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Добро пожаловать в онлайн-библиотеку<h1>'
                            '<img src="https://i.pinimg.com/474x/f8/a6/91/f8a6918cc87e710e9fef60d2dd670dc3.jpg"/>')

def system_time(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(f"<h1>Текущее время: {now}</h1>")