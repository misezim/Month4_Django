from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.basket_list_view, name='basket_list'),
    path('add_order/', views.add_order, name='add_order'),
    path('basket_list/<int:id>/delete/',views.delete_order, name = 'delete_order' ),
    path('basket_list/<int:id>/update/',views.update_order, name = 'update_order' ),

]