from django.shortcuts import render

# Create your views here.
def mynotes(request):
    return render(request, "mynotes/notes.html")
def notes_collection(request):
    return render(request, "mynotes/notes_collection.html", {'collection':'collection'})
