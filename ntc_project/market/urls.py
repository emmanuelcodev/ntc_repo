from django.urls import path
from .import views

app_name = 'market'

urlpatterns = [
    path('', views.notes_that_match_category, name = 'market_homepage'),
    path('<slug:category_slug>', views.notes_that_match_category, name = 'notes_that_match_category'),
    path('search/', views.search, name = 'search_from_query'),
    path('<slug:cat_slug>/<slug:note_slugg>', views.show_specific_note, name = 'specific_note'),
    path('<slug:cat_slug>/<slug:note_slugg>/<int:preview>', views.show_specific_note, name = 'preview_note'),

]
