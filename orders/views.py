from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


#<<<--------------------Список-------------------->>>
@method_decorator(cache_page(60*15), name='dispatch')
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = models.BasketModel

    def get_queryset(self):
        # return self.model.objects.all().order_by('-id')-----> Переписываем
        basket = cache.get('basket')
        if not basket:
            basket = self.model.objects.all().order_by('-id')
            cache.set('basket', basket, 60 * 15)
        return basket

# def basket_list_view(request):
#     if request.method == 'GET':
#         query = models.BasketModel.objects.all().order_by('-id')
#         context_object_name = {
#             'basket_list': query,
#         }
#         return render(request, template_name='basket/basket_list.html',
#                       context=context_object_name)




#<<<------------------------------Create------------------------->>>
class CreateOrderView(generic.CreateView):
    template_name = 'basket/create_order.html'
    form_class = forms.BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        response = super(CreateOrderView, self).form_valid(form=form)
        cache.delete('basket')
        return response

# def add_order(request):
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = forms.BasketForm()
#     return render(request, template_name='basket/create_order.html', context = {'form': form})




#<<<-----------------------------Удаление----------------------------->>>
class DeleteOrderView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'

    def get_object(self, *args, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=order_id)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        cache.delete('basket')
        return super().delete(request, *args, **kwargs)


#
# def delete_order(request, id):
#     order_id = get_object_or_404(models.BasketModel, id = id)
#     order_id.delete()
#     return redirect('basket_list')



#<<<-----------------------------Редактировать----------------------------->>>
class UpdateOrderView(generic.UpdateView):
    template_name = 'basket/update_order.html'
    form_class = forms.BasketForm
    success_url = '/basket_list/'

    def get_object(self, *args, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id= order_id)

    def form_valid(self, form):
        response = super(UpdateOrderView, self).form_valid(form=form)
        cache.delete('basket')
        return response


# def update_order(request, id):
#     order_id = get_object_or_404(models.BasketModel, id=id)
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = forms.BasketForm(instance=order_id)
#     return render(request, template_name='basket/update_order.html',
#                   context = {
#                       'form': form,
#                       'order_id' : order_id,
#                   })