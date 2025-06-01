from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
    path('daily-sales/', views.daily_sales, name='daily_sales'),
]
