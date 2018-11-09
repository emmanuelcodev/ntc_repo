from django.shortcuts import render, get_object_or_404
import os
from .models import Notes, Category
from django.core.paginator import Paginator,EmptyPage, InvalidPage
from django.db.models import Q

# Create your views here.
def test_index(request):
    return render(request, os.path.join('market', 'market.html'), {'market':'market'})


def notes_that_match_category(request, category_slug = None):

    category = None
    notes_list = None

    if category_slug!= None:
        category  = get_object_or_404(Category, cat_slug = category_slug)
        notes_list = Notes.objects.filter(note_category = category)#get notes that match a specific category
    else:
        notes_list = Notes.objects.all() #get all notes

    paginator = Paginator(notes_list, 9)
    print('paginator is ', paginator)

    try:
        page = int(request.GET.get('page','1'))

    except:
        page = 1


    try:
        notes = paginator.page(page)
        print(notes)
    except (EmptyPage, InvalidPage):
        notes = paginator.page(paginator.num_pages)

    return render(request, os.path.join('market', 'market.html'), {'market':'market', 'category':category, 'notes':notes, 'random_list': [[1,2,3], [4,5,6], [7,8,9]]})


#for when user makes a search --> leads to A) new page for search result OR B) 404 page
def search(request):
    #show nothing if user enters blank search result
    notes_list = None
    query = None
    error_message = None
    #if user actualy enters a query, grab it
    if 'user_query' in request.GET:
        query = request.GET.get('user_query')
        #checks if search is in name of product, summary of product, or category
        notes_list = Notes.objects.all().filter(Q(note_name__contains = query)|Q(note_summary__contains = query)|Q(category__cat_name__contains = query))

        if len(notes_list) == 0: #if no results
            #if no results, make error message and take them to new page
            #make error message and print it out on page only if got back empty query
            error_message = 'Sorry there were no results for your search term\n Try entering another term.'
            return render(request, os.path.join('market', 'no_results.html'), {'error_message': error_message})
        else:
            paginator = Paginator(notes_list, 9)

            #get correct page to display
            try:
                page = int(request.GET.get('page','1'))

            except:
                page = 1
            #get correct notes product for correct page
            try:
                notes = paginator.page(page)
                print(notes)
            except (EmptyPage, InvalidPage):
                notes = paginator.page(paginator.num_pages)


            return render(request, os.path.join('market', 'market_after_search.html'), {'query':query, 'notes':notes})


#To preview Individual content


#for Individual page content
def show_specific_note(request, cat_slug, note_slugg, preview = 0):

    try:
        print('\n\n\n\n\nworking great so far1')

        note = Notes.objects.get(category__slug=cat_slug, slug = note_slugg)

    except Exception as ewhoop:
        print('except printing out')
        raise ewhoop



    if preview == 0:
        return render(request, 'market/specific_note.html', {'specific_note':'specific_note', 'note':note})
    else:
        return render(request, 'market/note_preview.html', {'note_preview':'preview_note', 'note':note})

'''

def search(request):
    #show nothing if user enters blank search result
    notes = None
    query = None
    #if user actualy enters a query, grab it
    if 'user_query' in request.GET:
        query = request.GET.get('user_query')
        #checks if search is in name of product, summary of product, or category
        notes = Notes.objects.all().filter(Q(note_name__contains = query)|Q(note_summary__contains = query)|Q(note_category__cat_name__contains = query))
        print('working in the if part')
        print(notes)
        print('hello')
        return render(request, os.path.join('market', 'market_after_search.html'), {'query':query, 'notes':notes})
    else:
        print('working in the else part')
        return render(request, os.path.join('market', 'market_after_search.html'))



'''
