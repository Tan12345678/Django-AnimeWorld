from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'Home.html')
def Anime(request):
    return render(request,'index.html')
def AnimeHindi(request):
    return render(request,'AnimeHindi.html')