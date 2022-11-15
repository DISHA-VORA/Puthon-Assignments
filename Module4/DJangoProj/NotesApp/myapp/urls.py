# from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('userLogout/',views.userLogout),
    path('updateProfile/',views.updateProfile),
    path('about/',views.about),
    path('contact/',views.contact),
    path('shownotes/',views.shownotes),
]