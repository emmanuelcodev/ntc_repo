from django.shortcuts import render, get_object_or_404
import os
# Create your views here.
def test_index(request):
    return render(request, os.path.join('market', 'market.html'), {'market':'market'})


def notes_that_match_category(request, category_slug = None):

    category = None
    notes = None

    if category_slug!=None:
        category  = get_object_or_404(Category, cat_slug = category_slug)
        notes = Notes.objects.filter(note_category = category)#get notes that match a specific category
    else:
        notes = Notes.objects.all() #get all notes

    return render(request, os.path.join('market', 'market.html'), {'market':'market', 'category':category, 'notes':notes})
