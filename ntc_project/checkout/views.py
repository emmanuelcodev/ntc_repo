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
    cart_items_add = []
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



    #prepare message with product notes price total price put into a string
    items_bought_message ='Subject: Thank you for your purchase.\nYour new notes have added to your account.\n Below your purchases'

    for x in cart_notes_ids:

        items_bought_message+= '\n'
        items_bought_message+= '--------------------------------------\n'
        items_bought_message+= 'Product Name:  ' + str(x.note.note_name) + '\n'
        items_bought_message+= 'Product Price: ' + str(x.note.note_price) + '\n'
        items_bought_message+= 'Product Rating:' + str(x.note.ratings) + '\n'
        items_bought_message+= '\n'
    items_bought_message+= 'Total                             ' +str(sum_of_price)


    import smtplib
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    type(smtpObj)
    smtpObj.ehlo()
    smtpObj.starttls()

    smtpObj.login(' notetakingcenter@gmail.com ', ' jump2828 ')
    smtpObj.sendmail(' notetakingcenter@gmail.com ', ' notetakingcenter@gmail.com ',
    'Subject: Thank you for your purchase.\nYour new notes have added to your account.' + items_bought_message)
    smtpObj.quit()
    '''
    from django.core.mail import send_mail

    send_mail(
        'Review Your Purchase',
        items_bought_message,
        from_email = 'notetakingcenter@gmail.com',
        recipient_list = ['notetakingcenter@gmail.com'],
        auth_user ='notetakingcenter@gmail.com',
        auth_password = 'jump2828',
        fail_silently=False,
    )

    '''

    for x in cart_notes_ids:
        cart_item_removing = CartItems.objects.get(id=x.id)
        cart_item_removing.delete()

    print(items_bought_message)
    return redirect(to = 'mynotes:mynotes')
