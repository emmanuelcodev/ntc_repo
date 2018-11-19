from django.shortcuts import render, redirect, reverse
from .models import CartItems
from market.models import Notes

# Create your views here.
def cart(request):
    cart_items_test_list = []
    cart_notes_ids = CartItems.objects.all()
    sum_of_price = 0
    for x in cart_notes_ids:
        cart_items_test_list.append(x)
        sum_of_price += x.note.note_price
    print(sum_of_price)
    print(cart_items_test_list)


    return render(request, "cart/cart.html" , {'cart':'cart', 'cart_items':cart_items_test_list, 'sum_of_price':sum_of_price})

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
    return redirect(to = 'cart:cart')

def remove_cart(request, cart_id, dummy):
    cart_item_removing = CartItems.objects.get(id=cart_id)
    cart_item_removing.delete()
    return redirect(to = 'cart:cart')
    #return redirect(to='detail', product_id=product.id)
