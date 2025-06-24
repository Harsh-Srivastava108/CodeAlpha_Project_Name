from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Job Board!</h1><p>Go to <a href='/jobs/'>Jobs</a></p>")
