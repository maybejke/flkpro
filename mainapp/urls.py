from django.urls import path

from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('allproducts/', mainapp_views.allproducts, name='allproducts'),
    path('reception/', mainapp_views.reception, name='reception'),
    path('kitchen/', mainapp_views.kitchen, name='kitchen'),
    path('arch/', mainapp_views.arch, name='arch'),
    path('special/', mainapp_views.special, name='special'),
    path('tables/', mainapp_views.tables, name='tables'),
    path('decor/', mainapp_views.decor, name='decor'),
    path('living/', mainapp_views.living, name='living'),
]
