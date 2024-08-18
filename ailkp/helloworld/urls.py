from django.urls import path
from . import views

#3.Adim : Uygulamanın urls.py dosyasını oluşturduk ve içeriğini yazdık.
urlpatterns = [
    path('httpresponse/', views.httpresponse, name='htppresponse'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
