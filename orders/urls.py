from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.BasketListView.as_view(), name='basket_list'),
    path('add_order/', views.CreateOrderView.as_view(), name='add_order'),
    path('basket_list/<int:id>/delete/',views.DeleteOrderView.as_view(), name = 'delete_order' ),
    path('basket_list/<int:id>/update/',views.UpdateOrderView.as_view(), name = 'update_order' ),

]