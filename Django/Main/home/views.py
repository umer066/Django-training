from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render (request,'index.html')
    return HttpResponse ("This is Home-page")

def about(request):
    return HttpResponse ("This is About-page")

def services(request):
    return HttpResponse ("This is Services-page")

def contact(request):
    return HttpResponse ("This is Contact-page")