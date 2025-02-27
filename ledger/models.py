from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.id])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField
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
