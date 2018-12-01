from django.shortcuts import render
from .models import CreditCards


# Create your views here.

def setting_payment(request):
    print('inside of settings_payment')
    if request.method=="POST":
        newPassword= request.POST['newPassword']
        print(newPassword)
        confirmNewPassword= request.POST['confirmNewPassword']
        print(confirmNewPassword)
        currentPassword= request.POST['currentPassword']
        print(currentPassword)
        if newPassword == confirmNewPassword and newPassword != '' and currentPassword !='':
            message = 'Password has been changed'
        else:
            message = 'Passwords do not match, try again'
        return render(request,'settings/SettingAccount.html',{'message':message})
    return render(request,'settings/SettingAccount.html')

def policy_payment(request):

    return render(request,'settings/PolicyAccount.html')

def payment_payment(request):
    credit_cards = CreditCards.objects.all()
    print(credit_cards)

    if request.method=="POST":
        #read data from page,
        #check to make sure it is not empty
        #if it is not empty save information
        #print out message Try again
        firstname = request.POST['firstname']
        print(firstname)
        email = request.POST['email']
        print(email)
        address = request.POST['address']
        print(address)
        city = request.POST['city']
        print(city)
        state = request.POST['state']
        print(state)
        zip = request.POST['zip']
        print(zip)
        cardname = request.POST['cardname']
        print(cardname)
        cardnumber = request.POST['cardnumber']
        print(cardnumber)
        expmonth = request.POST['expmonth']
        print(expmonth)
        expyear = request.POST['expyear']
        print(expyear)
        cvv = request.POST['cvv']
        print(cvv)


        #check to make sure it is not empty
        if firstname != '' and email !=''and address !=''and city !=''and state !=''and zip !=''and cardname !=''and cardnumber !=''and expmonth !=''and expyear!='' and cvv!='' :
            #if it is not empty save information
            credit_card = CreditCards.objects.create(fullName=firstname,nameOnCard=cardname,email=email,address=address,city=city,zip=zip,states=state,creditCardNum=cardnumber,expmonth=expmonth,cvv=cvv,expYear=expyear)
            credit_card.save()
            print(credit_card)
            print(type(credit_card))

            message = 'Credit card has been saved'
            print('\n\nworked bro')
        else:
            #print out message Try again
            message = 'All information must be filled out, try again'
            print('\n\n inside try again')

        return render(request,'settings/PaymentAccount.html',{'payment':'payment','cards':credit_cards, 'message':message})
    return render(request,'settings/PaymentAccount.html',{'payment':'payment','cards':credit_cards})
