from django.shortcuts import render,redirect
from django.views import generic

from . import models, forms

# PARSER Book LIST
class MybookListView(generic.ListView):
    template_name = 'parser_appl/mybook_list.html'
    context_object_name = 'mybook'
    model = models.MybookModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')

# PARSER FILM LIST
class RezkaListView(generic.ListView):
    template_name = 'parser_appl/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel
    success_url = '/rezka_list/'


    def get_queryset(self):
        return self.model.objects.all().order_by('id')

# FORM PARSER
class MybookFormView(generic.FormView):
    template_name = 'parser_appl/mybook_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            if form.data['media_type'] == 'rezka.ag':
                return redirect('rezka_list')  # Перенаправление на страницу с фильмами
            else:
                return redirect('mybook_list')  # Перенаправление на страницу с книгами
        else:
            return super(MybookFormView, self).post(request, *args, **kwargs)


