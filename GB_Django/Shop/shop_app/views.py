from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, FormView,View,CreateView
from .models import Client, Order, Product
from .forms import AddProductForm
from django.contrib import messages

# Create your views here.

class IndexPageView(TemplateView):
    """
    Представление стартовой страницы
    """
    template_name = 'index.html'



class AddNewProductView(TemplateView):
    """
    Предстевление страницы добвления продукта
    """
    template_name = 'new_product.html'
    

class AddNewProductFormView(FormView):
    """
    Предствление формы добавления продукта
    """
    def post(self,request,*args, **kwargs):
        """
        Добавление продукта из формы
        """
       
        