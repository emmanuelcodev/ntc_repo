from django.shortcuts import render

# Create your views here.
def mynotes(request):
    return render(request, "mynotes/notes.html")
def notesContent(request):
    return render(request, "mynotes/notesContent.html")
