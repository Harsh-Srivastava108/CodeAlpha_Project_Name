from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_home, name='reservation_home'),
]
