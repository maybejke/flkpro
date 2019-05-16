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

    first_pages = Image.objects.filter(is_active=True, category__name='kitchen')

    content = {
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/kitchen.html', content)


def arch(request):

    first_pages = Image.objects.filter(is_active=True, category__name='arch')

    content = {
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/arch.html', content)


def special(request):

    first_pages = Image.objects.filter(is_active=True, category__name='special')

    content = {
        'first_pages': first_pages,
    }
    return render(request, 'mainapp/special.html', content)


def tables(request):

    first_pages = Image.objects.filter(is_active=True, category__name='tables')

    content = {
        'first_pages': first_pages,
    }
    return render(request, 'mainapp/tables.html', content)


def decor(request):

    first_pages = Image.objects.filter(is_active=True, category__name='decor')

    content = {
        'first_pages': first_pages,
    }
    return render(request, 'mainapp/decor.html', content)


def living(request):

    first_pages = Image.objects.filter(is_active=True, category__name='living')

    content = {
        'first_pages': first_pages,
    }
    return render(request, 'mainapp/living.html', content)
