from django.urls import path
from . import views

urlpatterns =[
 
path('', views.IndexPageView.as_view(), name="index"),
path("all_orders/", views.AllOrdersView.as_view(), name="all_orders")
]