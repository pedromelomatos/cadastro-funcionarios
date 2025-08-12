from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def logar(request:HttpRequest):
    return render(request, 'login.html')