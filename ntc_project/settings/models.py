from django.db import models

class CreditCards(models.Model):
    fullName = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    address = models.CharField(max_length = 60)
    city  = models.CharField(max_length = 60)
    zip  = models.CharField(max_length = 60)
    states  = models.CharField(max_length = 60)
    nameOnCard = models.CharField(max_length = 60)
    creditCardNum = models.CharField(max_length = 60)
    expmonth = models.CharField(max_length = 60)
    cvv = models.CharField(max_length = 60)
    expYear = models.CharField(max_length = 60)

    def credit_card_id(self):
        return self.id

# Create your models here.
