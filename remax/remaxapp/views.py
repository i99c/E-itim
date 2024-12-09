from django.shortcuts import render

def base(request):
      return render(request, 'base.html')

def soru(request):
      return render(request, "soru.html")

def sinif(request):
      return render(request, "sinif.html")

def login(request):
      return render(request, "login.html")

def register(request):
      return render(request, "register.html")