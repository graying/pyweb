from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    category_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.category_text

class Ingredient(models.Model):
    ingredient_text = models.CharField(max_length = 200)
    ingredient_text_cn = models.CharField(max_length = 200)
    def __str__(self):
        return self.ingredient_text

class Menuitem(models.Model):
    menuitem_text = models.CharField(max_length = 200)
    menuitex_text_cn = models.CharField(max_length = 200, default='Chinese name')
    price = models.FloatField(default = 0)
    #0-non spicy, 1-mild spicy, 2-very spicy
    spicy_level = models.IntegerField(default = 0)
    is_vegetarian = models.BooleanField(default = False)
    ingredient = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category)
    menuimage = models.ImageField(upload_to='menuimage/', default='menuimage/default.png')
    def __str__(self):
        return self.menuitem_text
