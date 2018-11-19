from django.db import models
from market.models import Notes
from django.urls import reverse
# Create your models here.


class CartItems(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, unique=True)

    def cart_item_id(self):
        return self.id
    def remove_cart_item_url(self):
        return reverse('cart:remove_cart', args=[self.cart_item_id(),"sup"])
