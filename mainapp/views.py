from django.shortcuts import render
from .models import Image


# Create your views here.


def index(request):

    first_pages = Image.objects.filter(is_active=True, category__name='all')

    content = {
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/index.html', content)


def reception(request):

    first_pages = Image.objects.filter(is_active=True, category__name='reception')

    content = {
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/reception.html', content)


def kitchen(request):
    return render(request, 'mainapp/kitchen.html')


def arch(request):

    first_pages = Image.objects.filter(is_active=True, category__name='arch')

    content = {
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/arch.html', content)


def special(request):
    return render(request, 'mainapp/special.html')


def tables(request):
    return render(request, 'mainapp/tables.html')


def decor(request):
    return render(request, 'mainapp/decor.html')


def living(request):
    return render(request, 'mainapp/living.html')
