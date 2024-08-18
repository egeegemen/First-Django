from django.urls import path
from . import views

#3.Adim : Uygulamanın urls.py dosyasını oluşturduk ve içeriğini yazdık.
urlpatterns = [
    path('', views.index, name='index'),
    path('aaaa/', views.index, name='index')
]
