from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Ingredient, Menuitem

# Register your models here.

class MenuitemAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.menuimage.url))

    image_tag.short_description = 'menuimage'

    list_display = ['image_tag',]

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Menuitem)
