from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#4.Adim : views.py dosyasına index fonksiyonunu ekledik.
def httpresponse(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html') # 5.Adim : render fonksiyonu ile index.html dosyasını çağırdık.

def about(request):
    return render(request, 'about.html') # 6.Adim : render fonksiyonu ile about.html dosyasını çağırdık.