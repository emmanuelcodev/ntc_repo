from django.db import models

# Create your models here.

class MyPurchases(models.Model):
    notes_id = models.IntegerField(default=True)

    def notes_id_f(self):
        return id
