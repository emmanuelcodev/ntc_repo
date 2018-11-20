from django.shortcuts import render,redirect
from .models import MyPurchases
from market.models import Notes, Comment
from datetime import datetime

# Create your views here.
def mynotes(request):
    ids_list = []
    #Grabbing the note ids that the user already purchased
    purchases_notes_ids = MyPurchases.objects.all()
    for x in purchases_notes_ids:
        ids_list.append(x.notes_id)

    print(ids_list)
    print(purchases_notes_ids)

    #Grab the note objects that correspond to the ids of notes already purchased by user
    notes_purchased_list = []
    for x in ids_list:
        print(x)
        notes_purchased_list.append(Notes.objects.get(id=x))

    print(notes_purchased_list)

    return render(request, "mynotes/notes.html", {'mynotes':'mynotestest','ids':ids_list,'notes_purchased':notes_purchased_list})




def selected_note(request, mynotes_id):

    note = Notes.objects.get(id=mynotes_id)

    return render(request, 'mynotes/notes_collection.html', {'selected_note':'selected_note', 'note':note})

def make_review(request, notes_id=None):
    #Generate new rating that includes user start rating
    if request.method == "POST":
        message = request.POST["review"]
        star_rating = request.POST.get("rating")
        print(message)
        if message == "" or star_rating == None:
            error_message = "Both comment and star rating need to be filled out before submitting."
            print("")
            return redirect(to = 'mynotes:mynotes')
        else:
            if star_rating == "star-1":
                rating = 1
            elif star_rating == "star-2":
                rating = 2
            elif star_rating == "star-3":
                rating = 3
            elif star_rating == "star-4":
                rating = 4
            else:
                rating = 5
            # Puts rating and comment algorithm
            note_comments = Comment.objects.all().filter(product_id = notes_id)

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
                # Add rating that user is making
                if rating == 1:
                    note_info['one_star'] += 1
                elif rating == 2:
                    note_info['two_star'] += 1
                elif rating == 3:
                    note_info['three_star'] += 1
                elif rating == 4:
                    note_info['four_star'] += 1
                else:
                    note_info['five_star'] += 1
                #get overall rating
                overal_rating = round(((note_info['one_star']*1) + (note_info['two_star']*2) + (note_info['three_star']*3) + (note_info['four_star']*4) + (note_info['five_star']*5)) /(general_info[0]), 2)
                # Add Comment to database
                user_comment = Comment.objects.create(buyer_user="IAlan",buyer_rating=rating, buyer_commentary=message, date_created=datetime.now(), product_id=notes_id)
                user_comment.save()
                #updating overall note rating
                note_being_reviewed = Notes.objects.all().filter(id=notes_id)
                note_being_reviewed.ratings = overal_rating
                
    #Add comment to comment table
    print("inside make review")
    return redirect(to = 'mynotes:mynotes')
