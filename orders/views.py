from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#Список покупок
def basket_list_view(request):
    if request.method == 'GET':
        query = models.BasketModel.objects.all().order_by('-id')
        context_object_name = {
            'basket_list': query,
        }
        return render(request, template_name='basket/basket_list.html',
                      context=context_object_name)

#Добавление покупок
def add_order(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/create_order.html', context = {'form': form})

#Удаление
def delete_order(request, id):
    order_id = get_object_or_404(models.BasketModel, id = id)
    order_id.delete()
    return redirect('basket_list')

#Редактировать
def update_order(request, id):
    order_id = get_object_or_404(models.BasketModel, id=id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm(instance=order_id)
    return render(request, template_name='basket/update_order.html',
                  context = {
                      'form': form,
                      'order_id' : order_id,
                  })