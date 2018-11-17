from django.shortcuts import render, redirect
from .models import CartItems
from market.models import Notes

# Create your views here.
def cart(request):
    return render(request, "cart/cart.html" , {'cart':'cart'})

def add_to_cart(request,product_id):
    #add to table
    print('in where i need to be cart views add_to_cart')
    #get Notes Item Associated with Cart Item
    note = Notes.objects.get(id = product_id)
    #create CartItem object


    try:
        carti = CartItems.objects.create(note = note)
        carti.save()

    except:
        pass

    #cart_items = CartItems.objects.get
    #return redirect('product_detail', product_id=product_id)
    return render(request, "cart/cart.html" , {'cart':'cart'})
