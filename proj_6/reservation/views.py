from django.http import HttpResponse

def reservation_home(request):
    return HttpResponse("Reservation dashboard")
