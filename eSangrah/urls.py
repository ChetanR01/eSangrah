from django.contrib import admin
from django.urls import path
from eSangrah import views

urlpatterns = [
    path("", views.index, name='eSangrah'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("fruits", views.fruits, name='fruits'),
    path("dryfruit", views.dryfruit, name='dryfruit'),
    path("vegetable", views.vegetable, name='vegetable'),
    path("dailyneed", views.dailyneed, name='dailyneed'),
    path("electronics", views.electronics, name='electronics'),
    path("stationary", views.stationary, name='stationary'),
    path("xerox", views.xerox, name='xerox'),

    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path("cart", views.cart, name='cart'),

]

