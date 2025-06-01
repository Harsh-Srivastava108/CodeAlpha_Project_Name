from django.http import JsonResponse
from django.db.models import F, Sum, ExpressionWrapper, FloatField
from datetime import date
from orders.models import OrderItem
from django.shortcuts import render


def reports_home(request):
    return render(request, 'reports/reports_home.html')


def daily_sales(request):
    today = date.today()
    
    total = OrderItem.objects.filter(order__order_date__date=today).annotate(
        item_total=ExpressionWrapper(F('quantity') * F('item__price'), output_field=FloatField())
    ).aggregate(total_sales=Sum('item_total'))['total_sales']

    return JsonResponse({'total_sales': total or 0})
