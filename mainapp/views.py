from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')

def allproducts(request):
    return render(request, 'mainapp/app/view/allproducts.html')

def reception(request):
    return render(request, 'mainapp/app/view/reception.html')