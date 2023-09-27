from django.contrib import admin
from django.urls import path
from eSangrah import views

urlpatterns = [
    path("", views.index, name='eSangrah'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("fruits", views.fruits, name='fruits'),
    path("electronics", views.electronics, name='electronics'),
    path("prints", views.prints, name='prints'),

    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path('logout', views.logout, name='logout')

]

