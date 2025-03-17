from django.http import HttpResponse
def greet(request):
    return HttpResponse("Hello, Django!")
def myapp_home(request):
    return HttpResponse("Welcome to MyApp!")
