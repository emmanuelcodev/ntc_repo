from django.urls import path
from .import views

app_name = 'market'

urlpatterns = [
    path('', views.test_index, name = 'market'),
    path('<slug:category_slug>', views.notes_that_match_category, name = 'notes_that_match_category'),

    #
]
