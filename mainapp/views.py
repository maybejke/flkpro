from django.shortcuts import render
from .models import Image


# Create your views here.


def getFirstImage(category):
    first_image = Image.objects.filter(is_active=True, category__name=category).order_by('id').reverse()
    return list(first_image)[0]


def index(request):
    category = 'all'

    first_image = getFirstImage(category)
    first_pages = Image.objects.filter(is_active=True, category__name='all').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/index.html', content)


def reception(request):
    category = 'reception'

    first_image = getFirstImage(category)
    first_pages = Image.objects.filter(is_active=True, category__name='reception').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/reception.html', content)


def kitchen(request):
    category = 'kitchen'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='kitchen').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/kitchen.html', content)


def arch(request):
    category = 'arch'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='arch').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/arch.html', content)


def special(request):
    category = 'special'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='special').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/special.html', content)


def tables(request):
    category = 'tables'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='tables').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/tables.html', content)


def decor(request):
    category = 'decor'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='decor').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }

    return render(request, 'mainapp/decor.html', content)


def living(request):
    category = 'living'

    first_image = getFirstImage(category)

    first_pages = Image.objects.filter(is_active=True, category__name='living').order_by('id').reverse()

    content = {
        'first_image': first_image,
        'first_pages': first_pages,
    }
    return render(request, 'mainapp/living.html', content)
