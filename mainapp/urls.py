from django.urls import path

from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('allproducts/', mainapp_views.allproducts, name = 'allproducts'),
    path('reception/', mainapp_views.reception, name = 'reception'),
    # path('/kitchen', {controller:'kitchen', templateUrl: 'app/view/kitchen.html'}),
    # path('/arch', {controller:'arch', templateUrl: 'app/view/arch.html'}),
    # path('/special', {controller:'special', templateUrl: 'app/view/special.html'}),
    # path('/tables', {controller:'tables', templateUrl: 'app/view/tables.html'}),
    # path('/decor', {controller:'decor', templateUrl: 'app/view/decor.html'}),
    # path('/living', {controller:'living', templateUrl: 'app/view/living.html'}),
]
