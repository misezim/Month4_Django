from django.shortcuts import get_object_or_404, reverse
from . import models, forms
from django.views import generic

class RecipeListView(generic.ListView):
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipe_list'
    model = models.RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class CreateRecipeView(generic.CreateView):
    template_name = 'recipe/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form=form)

class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)

class RecipeDetailView(generic.UpdateView):
    template_name = 'recipe/recipe_detail.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_detail/<int:id>/'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id= recipe_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(RecipeDetailView, self).form_valid(form=form)


class CreateIngredientView(generic.CreateView):
    template_name = 'recipe/create_detail.html'
    form_class = forms.IngredientForm
    success_url = '/create_detail/<int:recipe_id>/'

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(models.RecipeModel, id=self.kwargs['recipe_id'])
        return super().form_valid(form)