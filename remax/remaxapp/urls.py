from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name='base'),
    path('soru/',views.soru, name='soru'),
    path('sinif/',views.sinif, name='sinif'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('katilimci/',views.katilimci, name='katilimci'),
]
