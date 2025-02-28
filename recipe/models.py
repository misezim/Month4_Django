from django.db import models

class RecipeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class IngredientModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Title")
    quantity = models.IntegerField(verbose_name="Quantity")
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'