from django.db import models
from django.urls import reverse

# Create your models here.

class MyPurchases(models.Model):
    notes_id = models.IntegerField(default=True, unique=True)

    def notes_id_f(self):
        return id
    def get_certain_notes_url(self):
        return reverse('mynotes:selected_note', args=[self.category.slug, self.slug, 1])
