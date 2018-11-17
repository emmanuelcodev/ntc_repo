from django.db import models
from market.models import Notes
# Create your models here.


class CartItems(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, unique=True)

    def cart_item_id(request):
        return id
