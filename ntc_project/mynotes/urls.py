from django.urls import path, include
from . import views

app_name = 'mynotes'

urlpatterns = [
    path('', views.mynotes,name="mynotes"),
    path('<int:mynotes_id>/', views.selected_note, name = 'selected_note'),
]
