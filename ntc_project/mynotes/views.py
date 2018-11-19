from django.shortcuts import render
from .models import MyPurchases
from market.models import Notes
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
