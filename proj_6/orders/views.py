

from django.shortcuts import render, redirect
from .models import MenuItem, Order
from .forms import OrderForm
from django.utils import timezone
from django.db.models import Sum

def orders_home(request):
    return render(request, 'orders/home.html') 

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'menu_items': items})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_order')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def daily_sales(request):
    today = timezone.now().date()
    orders = Order.objects.filter(order_date__date=today)
    total_sales = sum([order.total_amount for order in orders])
    return render(request, 'orders/daily_sales.html', {
        'orders': orders,
        'total_sales': total_sales
    })
