from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
def index_my(request):
    print("Get it")
    return HttpResponse("This is index function in views.py, which called by http://127.0.0.1:8000/my_polls_app/")
