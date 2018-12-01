from django.shortcuts import render, redirect, reverse
from cart.models import CartItems
from market.models import Notes
from settings.models import CreditCards
from mynotes.models import MyPurchases

# Create your views here.

def checkout(request):
    cart_items_test_list = []
    cart_notes_ids = CartItems.objects.all()
    sum_of_price = 0
    for x in cart_notes_ids:
        cart_items_test_list.append(x)
        sum_of_price += x.note.note_price
    print(sum_of_price)
    print(cart_items_test_list)

    credit_cards = CreditCards.objects.all()

    return render(request, "checkout/checkout.html" , {'checkout':'checkout', 'cards':credit_cards, 'sum_of_price':sum_of_price})



def make_payment(self):
    user_name = 'Alan Garcia'
    credit_card = CreditCards.objects.get(id=1)

    #load everything from the cart
    cart_items_add_to_purchases_id = []
    cart_notes_ids = CartItems.objects.all()
    sum_of_price = 0
    for x in cart_notes_ids:
        cart_items_add_to_purchases_id.append(x.note.prod_id())
        sum_of_price += x.note.note_price
    print(sum_of_price)
    #new line





    #add everything to mynotes because you own it now
    for x in cart_items_add_to_purchases_id:
        purchased_note_id = MyPurchases.objects.create(notes_id=x)
        purchased_note_id.save()
    #call method to send email message

    return redirect(to = 'mynotes:mynotes')
