from django.shortcuts import render
from .models import Image


# Create your views here.


def index(request):

    main_images = Image.objects.filter(is_active=True, category__is_active=True)

    content = {
        'main_images': main_images,
    }
    return render(request, 'mainapp/index.html', content)


def allproducts(request):

    return render(request, 'mainapp/allproducts.html')


def reception(request):
    return render(request, 'mainapp/reception.html')


def kitchen(request):
    return render(request, 'mainapp/kitchen.html')


def arch(request):
    return render(request, 'mainapp/arch.html')


def special(request):
    return render(request, 'mainapp/special.html')


def tables(request):
    return render(request, 'mainapp/tables.html')


def decor(request):
    return render(request, 'mainapp/decor.html')


def living(request):
    return render(request, 'mainapp/living.html')
