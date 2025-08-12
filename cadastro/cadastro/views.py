from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest

def redirecionar(request:HttpRequest):
    return redirect('autenticacao:login')