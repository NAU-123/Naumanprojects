"""
URL configuration for Hello project.

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
"""
from django.contrib import admin
from django.urls import path
from myapp import views

admin.site.site_header = "Nauman's Icecream's Admin"
admin.site.site_title = "Nauman's Icecream's Admin Portal"
admin.site.index_title = "Welcome to Nauman's Icecream's"
urlpatterns = [
    path("",views.index,name="myapp"),
    path("admin/", admin.site.urls),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact")
]
