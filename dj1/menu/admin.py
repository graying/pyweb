from django.contrib import admin
from .models import Category, Ingredient, Menuitem

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Menuitem)
