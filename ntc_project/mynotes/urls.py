from django.urls import path, include
from . import views

app_name = 'mynotes'

urlpatterns = [
    path('mynotes/', views.mynotes,name="mynotes"),
    path('notes_collection/', views.notes_collection,name="notes_collection"),
]
