from django.shortcuts import render, get_object_or_404, redirect

def login(request):
    return render(request, 'login.html')