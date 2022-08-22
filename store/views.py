from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>Hello, world. You're at the bookstore index.</h2>")
