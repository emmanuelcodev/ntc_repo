from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length = 60, unique = True)
    cat_slug = models.SlugField(max_length=80,unique= True)
    cat_description = models.TextField(blank=True)

    def __str__(self):
        return self.cat_name

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])


    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Notes(models.Model):
    note_name = models.CharField(max_length=60, unique = True)
    note_slug = models.SlugField(max_length=80,unique= True)
    note_summary = models.TextField(blank=True)
    note_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note_price = models.DecimalField(max_digits =10, decimal_places = 2)
    note_snippet = models.ImageField(upload_to = 'Notes', blank = True)
    note_image1 = models.ImageField(upload_to = 'Notes', blank = True)
    note_image2 = models.ImageField(upload_to = 'Notes', blank = True)
    note_image3 = models.ImageField(upload_to = 'Notes', blank = True)
    note_date_created = models.DateTimeField(auto_now_add=True)
    note_updated= models.DateTimeField(auto_now= True)
    note_times_purchased = models.IntegerField(default=0)
    ratings = models.DecimalField(max_digits =3, decimal_places = 1)
    note_uploader_user = models.CharField(max_length=60, unique = True)

    class Meta:
        ordering = ('note_name',)
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

        def __str__(self):
            return self.cat_name

class Comment(models.Model):
    buyer_user = models.CharField(max_length=60, unique = True)
    buyer_rating = models.DecimalField(max_digits =3, decimal_places = 1)
    buyer_commentary = models.TextField(blank=True)
    seller_note_being_reviewed = models.ForeignKey(Notes, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
