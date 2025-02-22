from django.urls import path
from . import views

urlpatterns = [
    path('mybook_list/', views.MybookListView.as_view(), name='mybook_list'),
    path('mybook_parsing/', views.MybookFormView.as_view(), name='parser'),
    path('rezka_list/', views.RezkaListView.as_view(), name = 'rezka_list')
]