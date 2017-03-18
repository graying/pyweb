from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, HttpResponseRedirect
from .models import Menuitem, Ingredient, Category
from django.views import generic
from django.urls import reverse

# Create your views here.


class IndexView(generic.ListView):
    #model = Menuitem
    context_object_name = 'menuitem'
    template_name = 'menu/index.html'

    def get_queryset(self):
        return Menuitem.objects.all()


class CategoryView(generic.ListView):
    context_object_name = "category"
    template_name = 'menu/category.html'

    def get_queryset(self):
        return Category.objects.all()


def cat_detail(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    menuitem = Menuitem.objects.filter(category=cat)
    template_name = 'menu/catdetail.html'
    return render(request, 'menu/catdetail.html', {
        'menuitem': menuitem,
        'category_text': cat.category_text,
    })
