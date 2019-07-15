from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.read, name='home'),
    path('new/',views.new,name='new'),
    path('newblog/',views.create,name="newblog"),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name="delete"),
]
