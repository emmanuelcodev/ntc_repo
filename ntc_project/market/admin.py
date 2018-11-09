from django.contrib import admin

from .models import Category, Notes, Comment


# Register your models here.

class CategoryManager(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    prepopulated_fields = {'slug':('cat_name',)}
admin.site.register(Category, CategoryManager)


class NoteManager(admin.ModelAdmin):
    list_display = ['note_name', 'note_price','note_date_created', 'note_uploader_user']
    list_editable = ['note_price']
    prepopulated_fields = {'slug':('note_name',)}
    list_per_page = 30
admin.site.register(Notes, NoteManager)


class CommentManager(admin.ModelAdmin):
    #cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    #slugn = models.ForeignKey(Notes, on_delete=models.CASCADE)
    pass
    #list_display=['buyer_rating']
    #list_editable = ['buyer_rating']
    #list_per_page = 30
admin.site.register(Comment, CommentManager)
