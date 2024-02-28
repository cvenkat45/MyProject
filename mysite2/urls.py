"""
URL configuration for mysite2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# """
# from django.contrib import admin
from captcha_admin import admin
from django.urls import path, include
from mysite2 import views


urlpatterns = [path('', views.IndexView.as_view(), name="index"),
               path('link1', views.Link1View.as_view(), name="link1"),
               path('polls/', include('polls.urls')),
               path('admin/', admin.site.urls),
               path('', include('src.urls')),
               ]

admin.site.index_title = 'Welcome to Mysite2NR @ in mysite2/url.py'
admin.site.site_title = 'Mysite2NR Hi'
admin.site.site_header = 'Mysite2NR'
