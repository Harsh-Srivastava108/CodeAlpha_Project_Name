from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_home, name='orders_home'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.place_order, name='place_order'),
    path('reports/daily-sales/', views.daily_sales, name='daily_sales'),
]
