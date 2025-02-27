from django.db import models


class Ingredient(models.Model):
    name = models.charField(max_length=100)


class Recipe(models.Model):
    name = models.charField(max_length=100)


class RecipeIngredient(models.Model):
    quantity = models.IntegerField
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
