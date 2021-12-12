from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name= 'Home'),
    path("go", views.go, name= 'go'),
    path("contact", views.contact, name= 'contact'),
    path("signup", views.signup, name= 'signup'),
    path("signin", views.signin, name= 'signin'),
    path("piano", views.piano, name= 'piano'),
    path("notes", views.notes, name= 'notes'),
]
