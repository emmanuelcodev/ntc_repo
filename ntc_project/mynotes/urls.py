from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mynotes,name="mynotes"),
    path('notesContent', views.notesContent,name="notesContent"),
]
