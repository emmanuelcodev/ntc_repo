from django.shortcuts import render
import os
# Create your views here.
def test_index(request):
    return render(request, os.path.join('market', 'market.html'))
