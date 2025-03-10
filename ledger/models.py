from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.pk])
    

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete = models.CASCADE,
        default = 1,
        related_name='recipe'
        )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete = models.CASCADE,
        default = 1,
        related_name='ingredients'
        )
    