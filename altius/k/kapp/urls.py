from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("delete/<int:id1>",views.delete,name="delete"),
    path("add/",views.add,name="add"),
     
]
