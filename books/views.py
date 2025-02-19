from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime

from django.urls import reverse_lazy

from . import models, forms
from django.views import generic
#<<<------------------------Поиск------------------->>>
class SearchView(generic.ListView):
    template_name = 'book.html'

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



#<<<--------------------Список-------------------->>>
class BookListView(generic.ListView):
    template_name = 'book.html'
    model = models.BookModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def book_list_view(request):
#     if request.method == 'GET':
#         query = models.BookModel.objects.all().order_by('-id')
#         context_object_name = {
#             'book': query,
#         }
#         return render(request, template_name='book.html',
#                       context=context_object_name)




#<<<--------------------------Details---------------------->>
class BookDetailView(generic.DetailView):
    model = models.BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self,*args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.BookModel,id = book_id)

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         query = get_object_or_404(models.BookModel, id=id)
#         context_object_name = {
#             'book_id': query,
#         }
#         return render(request,
#                       template_name='book_detail.html',
#                       context=context_object_name)


#<<<------------------------------Create------------------------->>>
class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.CreateBookReviewForm

    def form_valid(self, form):
        book_id = form.instance.choice_show.id
        self.success_url = f'/book_detail/{book_id}/'
        return super(CreateReviewView, self).form_valid(form=form)


# def create_review_view(request):
#     if request.method == 'POST':
#         form = forms.CreateBookReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save()
#             return redirect ('book_detail', id=review.choice_show.id)
#     else:
#         form = forms.CreateBookReviewForm()
#     return render(request, template_name='create_review.html', context={'form': form})



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