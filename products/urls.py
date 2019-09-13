from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('index', views.products, name='products'),
    path('favorite/', views.favorite, name='favorite'),
    path('shopping-cart/', views.shopping, name='shopping-cart')
]