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


    

class AllOrdersView(ListView):
   """
   Представление страницы с отображением 
   всех заказов клиента  за неделю
   за месяц и за год
   Используется пользователь Vasya 
   т.к только для него были созданы 
   вручную заказы (через коммандс отображаются не слишком читабельно
   тк  используется цикл заполения тестовыми данными)
   """
   def get(self,request):
       user = Client.objects.get(name = "Vasya")
       orders_week = Order.objects.filter(client=user, order_date__gte='2024-02-01').all()
       orders_month = Order.objects.filter(client=user, order_date__gte='2024-01-08').all()
       orders_year = Order.objects.filter(client=user, order_date__gte='2023-02-08').all()
       
       return render(request, 'all_orders.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})


