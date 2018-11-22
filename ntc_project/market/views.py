from django.shortcuts import render, get_object_or_404
import os
from .models import Notes, Category, Comment
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
        #comments for specific note

        id_note = note.prod_id()

        print('id note is ', id_note)
        print('\n\n\n\n\nworking great so far1')

        print(type(id_note))
        note_comments = Comment.objects.all().filter(product_id = id_note)




        print('\n\n note comments \n\n', note_comments)

        if len(note_comments) < 1:
            print('inside empty query set')
            return render(request, 'market/note_preview.html', {'note_preview':'preview_note', 'note':note, 'no_comments': 'Be the first one to leave a comment'})
        else:
            general_info = [0,[],[],[],[],[]]
            #indexes: total ratings, 1 star, 2 star, 3 star, 4 star,5 star,
            for x in note_comments:
                #print(x.buyer_rating)
                general_info[0] = general_info[0] + 1
                general_info[int(x.buyer_rating)].append(x.buyer_rating)

            print(general_info[0], 'general_info')
            note_info = {}
            #make sure that each for each numeric metric 1,2,3,4,5 get accounted for
            if general_info[1]:
                note_info['one_star'] = len(general_info[1])
            else:
                note_info['one_star'] = 0

            if general_info[2]:
                note_info['two_star'] = len(general_info[2])
            else:
                note_info['two_star'] = 0

            if general_info[3]:
                note_info['three_star'] = len(general_info[3])
            else:
                note_info['three_star'] = 0

            if general_info[4]:
                note_info['four_star'] = len(general_info[4])
            else:
                note_info['four_star'] = 0

            if general_info[5]:
                note_info['five_star'] = len(general_info[5])
            else:
                note_info['five_star'] = 0
            #get overall rating

            overal_rating = round(((note_info['one_star']*1) + (note_info['two_star']*2) + (note_info['three_star']*3) + (note_info['four_star']*4) + (note_info['five_star']*5))/(general_info[0]), 2)
            
            star_lists = generate_star_info(overal_rating)
            print('complete_rating is ', star_lists[0], ' \n partial_rating is ', star_lists[1], '\n blank_rating is ', star_lists[2])

            #render page
            if star_lists[1]:
                return render(request, 'market/note_preview.html', {'note_preview':'preview_note', 'note':note, 'note_comments': note_comments, 'total_ratings':general_info[0],'one_star':note_info['one_star'], 'two_star':note_info['two_star'], 'three_star':note_info['three_star'], 'four_star':note_info['four_star'], 'five_star':note_info['five_star'], 'prog1':(note_info['one_star']/general_info[0])*100, 'prog2':(note_info['two_star']/general_info[0])*100, 'prog3':(note_info['three_star']/general_info[0])*100, 'prog4':(note_info['four_star']/general_info[0])*100, 'prog5':(note_info['five_star']/general_info[0])*100, 'overal_rating':overal_rating, 'complete_rating':star_lists[0], 'partial_rating':star_lists[1], 'blank_rating':star_lists[2]})
            else:
                return render(request, 'market/note_preview.html', {'note_preview':'preview_note', 'note':note, 'note_comments': note_comments, 'total_ratings':general_info[0],'one_star':note_info['one_star'], 'two_star':note_info['two_star'], 'three_star':note_info['three_star'], 'four_star':note_info['four_star'], 'five_star':note_info['five_star'], 'prog1':(note_info['one_star']/general_info[0])*100, 'prog2':(note_info['two_star']/general_info[0])*100, 'prog3':(note_info['three_star']/general_info[0])*100, 'prog4':(note_info['four_star']/general_info[0])*100, 'prog5':(note_info['five_star']/general_info[0])*100, 'overal_rating':overal_rating, 'complete_rating':star_lists[0],'blank_rating':star_lists[2]})

def generate_star_info(rating):
    complete_rating = int(rating)#need to know how many complete filled orange stars to print out
    remaining_rating = rating % complete_rating#need to know how paritally filled the star is next to the complete star
    blank_ratings = 5 - complete_rating #needed to know how many blank stars to put at the end
    print('inside function \n  complete_rating is ', complete_rating, ' \n partial_rating is ', remaining_rating, '\n blank_rating is ', blank_ratings)


    #put code for html code

    star_empty_list = []

    star_empty_list.append([0]*complete_rating)
    print('list is', star_empty_list)

    #check partiall filled star then add it at the end of html code
    if remaining_rating >= 0.01:
        star_empty_list.append([3])
    else:
        star_empty_list.append(None)
    print('list is after seconds', star_empty_list)
    #put empty stars at the end
    if len(star_empty_list[0]) <= 4: #only works if below four, because othersise will have 4 stars, 1 partial, and 1 blank
        if len(star_empty_list[0]) < 4:
            print('len working')

            if remaining_rating >=0.01:#if partial is not full need extra blanks
                    star_empty_list.append([0]*(blank_ratings-1))
            else:
                star_empty_list.append([0]*blank_ratings)

        else:#if four
            if remaining_rating >= 0.1:
                star_empty_list.append(None)
            else:
                star_empty_list.append([0])
    else:#if five
        star_empty_list.append(None)
    #    if star_empty_list[1]:#if partial is not full need extra blanks
    #        star_empty_list.append([0]*blank_ratings)
    #    else:
    #        star_empty_list.append([0]*(blank_ratings -1)) #if partial star exists then blank star is one less
    #        print('entire list is ', star_empty_list)
    print('so whole list inside of function is ', star_empty_list)
    return star_empty_list


'''
def generate_star_html(rating):
    complete_rating = int(rating)#need to know how many complete filled orange stars to print out
    remaining_rating = rating % complete_rating#need to know how paritally filled the star is next to the complete star
    blank_ratings = 5 - complete_rating #needed to know how many blank stars to put at the end

    #put code for html code
    star_html = ''
    for x in range(complete_rating):
        star_html += '<span class="rating" style="font-size:1.2em;">●</span>'

    #check partiall filled star then add it at the end of html code
    if remaining_rating >= 0.01 and remaining_rating <=1:
        star_html += '<span class="rating" style="font-size:1.2em;">◐</span>'

    #put empty stars at the end
    for x in range(blank_ratings):
        star_html += '<span class="rating_blank" style="font-size:1.2em;">○</span>'
    return star_html
'''
