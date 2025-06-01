from django.http import HttpResponse

def inventory_home(request):
    return HttpResponse("Welcome to the inventory section")
