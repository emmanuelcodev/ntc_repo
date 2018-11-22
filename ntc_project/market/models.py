from django.db import models
from django.urls import reverse
from django.template import Context, Template


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length = 60, unique = True)
    slug = models.SlugField(max_length=80,unique= True)
    cat_description = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.cat_name)

    def get_url(self):
        return reverse('market:products_by_category', args=[self.cat_slug])


    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Notes(models.Model):
    note_name = models.CharField(max_length=60, unique = True)
    slug = models.SlugField(max_length=80,unique= True)
    note_summary = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note_price = models.DecimalField(max_digits =10, decimal_places = 2)
    note_snippet = models.ImageField(upload_to = 'Notes', blank = True)
    note_image1 = models.ImageField(upload_to = 'Notes', blank = True)
    note_image2 = models.ImageField(upload_to = 'Notes', blank = True)
    note_image3 = models.ImageField(upload_to = 'Notes', blank = True)
    note_date_created = models.DateTimeField(auto_now_add=True)
    note_updated= models.DateTimeField(auto_now= True)
    note_times_purchased = models.IntegerField(default=0)
    ratings = models.DecimalField(max_digits =3, decimal_places = 1)

    note_uploader_user = models.CharField(max_length=60)

    def get_note_url(self):
        return reverse('market:specific_note', args=[self.category.slug, self.slug])
    def get_preview_url(self):
        return reverse('market:preview_note', args=[self.category.slug, self.slug, 1])
    def prod_id(self):
        return self.id
    def add_to_cart_url(self):
        return reverse('cart:add_to_cart', args=[self.prod_id()])
    def get_selected_note_url(self):
        return reverse('mynotes:selected_note', args=[self.prod_id()])
    def get_make_review_url(self):
        return reverse('mynotes:make_review', args=[self.prod_id()])
    def get_complete_star(self):
        star_html = generate_star_html(self.ratings)
        c = Context({"my_name": "Adrian"})
        return Template(star_html).render(c)



    class Meta:
        ordering = ('note_name',)
        verbose_name = 'note'
        verbose_name_plural = 'notes'

        def __str__(self):
            return '{}'.format(self.cat_name)





class Comment(models.Model):
    buyer_user = models.CharField(max_length=60, unique = False)
    buyer_rating = models.IntegerField(default=0)
    buyer_commentary = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField(default=0)

    def get_buyer_rating_star(self):
        star_html = generate_star_html(self.buyer_rating)
        c = Context({"my_name": "Adrian"})
        return Template(star_html).render(c)

    class Meta:
        ordering = ('date_created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'



def generate_star_html(rating):
    complete_rating = int(rating)#need to know how many complete filled orange stars to print out
    #BUG if raiting is 0.# it will not work because of the rating % complete_rating code, which will result in zero, display
    #   #all blank stars but infact needs a partial star, need a better wayto get partial star remainder
    if complete_rating == 0:
        star_html = ''
        star_html += ' <span class="rating" style="font-size:1.2em;"> ○</span> '
        star_html += ' <span class="rating" style="font-size:1.2em;"> ○</span> '
        star_html += ' <span class="rating" style="font-size:1.2em;"> ○</span> '
        star_html += ' <span class="rating" style="font-size:1.2em;"> ○</span> '
        star_html += ' <span class="rating" style="font-size:1.2em;"> ○</span> '
        return star_html

    remaining_rating = rating % complete_rating#need to know how paritally filled the star is next to the complete star
    blank_ratings = 5 - complete_rating #needed to know how many blank stars to put at the end
    #print('\n\n', self.prod_id, ' is what we are talkoing about ')
    #put code for html code
    star_html = ''
    for x in range(complete_rating):
        star_html += '<span class="rating" style="font-size:1.2em;">●</span>'

    #check partiall filled star then add it at the end of html code
    if remaining_rating >= 0.01 and remaining_rating <=1:
        star_html += '<span class="rating" style="font-size:1.2em;">◐</span>'

    #partial so now fill blanks

    if complete_rating <= 4: #only works if below four, because othersise will have 4 stars, 1 partial, and 1 blank
        if complete_rating < 4:
            print('len working')

            if remaining_rating >=0.01:#if partial is not full need extra blanks
                for x in range(blank_ratings - 1):
                    star_html += '<span class="rating" style="font-size:1.2em;">○</span>'
            else:
                for x in range(blank_ratings):
                    star_html += '<span class="rating" style="font-size:1.2em;">○</span>'


        else:#if four
            if remaining_rating >= 0.1:
                pass
            else:
                star_html += '<span class="rating" style="font-size:1.2em;">○</span>'
    else:#if five
        pass
    #print('star_html for ', self.prod_id, ' is ', star_html)
    #put empty stars at the end

    #for x in range(blank_ratings):
    #    star_html += '<span class="rating" style="font-size:1.2em;">○</span>'
    #print('star_html is: \n', star_html)
    return star_html
