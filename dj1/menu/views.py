from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from .models import Menuitem, Ingredient, Category
from django.views import generic
from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'menuitem'
    template_name = 'menu/index.html'
    def get_queryset(self):
        return Menuitem.objects.all()
