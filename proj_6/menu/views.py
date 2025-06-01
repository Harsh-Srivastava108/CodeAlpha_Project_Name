from django.http import HttpResponse

def menu_home(request):
    return HttpResponse("Menu items will be displayed here")
