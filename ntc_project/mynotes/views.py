from django.shortcuts import render
from .models import MyPurchases
from market.models import Notes
# Create your views here.
def mynotes(request):
    ids_list = []
    purchases_notes_ids = MyPurchases.objects.all()
    for x in purchases_notes_ids:
        ids_list.append(x)

    print(purchases_notes_ids)

    return render(request, "mynotes/notes.html", {'mynotes':'mynotestest','ids':ids_list})




def notes_collection(request):
    return render(request, "mynotes/notes_collection.html", {'collection':'collection'})
