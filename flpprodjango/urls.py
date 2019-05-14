"""flpprodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.index, name='index'),
    path('', include('mainapp.urls', namespace='index')),
    path('reception/', mainapp_views.reception, name='reception'),
    path('kitchen/', mainapp_views.kitchen, name='kitchen'),
    path('arch/', mainapp_views.arch, name='arch'),
    path('special/', mainapp_views.special, name='special'),
    path('tables/', mainapp_views.tables, name='tables'),
    path('decor/', mainapp_views.decor, name='decor'),
    path('living/', mainapp_views.living, name='living'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

