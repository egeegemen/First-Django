from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#4.Adim : views.py dosyasına index fonksiyonunu ekledik.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")