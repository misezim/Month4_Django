from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name = 'create_recipe'),
    path('recipe_list/<int:id>/delete/',views.DeleteRecipeView.as_view(), name = 'delete_recipe' ),
    path('recipe_detail/<int:id>/',views.RecipeDetailView.as_view(),name = 'recipe_detail' ),
    path('create_detail/<int:recipe_id>/', views.CreateIngredientView.as_view(), name = 'create_detail'),
]

