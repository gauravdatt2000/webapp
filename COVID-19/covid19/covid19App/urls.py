from django.contrib import admin
from django.urls import path
from covid19App import views
urlpatterns = [
    path("",views.index,name='covid19'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("country",views.country,name='country')
]