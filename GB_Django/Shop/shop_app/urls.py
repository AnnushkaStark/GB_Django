from django.urls import path
from . import views

urlpatterns =[
 
path('', views.IndexPageView.as_view(), name="index"),
path('new_product/', views.AddNewProductView.as_view(), name = 'new_product'),
path("new_product_form/", views.AddNewProductFormView.as_view(), name="new_product_form")
]