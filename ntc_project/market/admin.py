from django.contrib import admin

from .models import Category, Notes


# Register your models here.

class CategoryManager(admin.ModelAdmin):
    list_display = ['cat_name', 'cat_slug']
    prepopulated_fields = {'cat_slug':('cat_name',)}
admin.site.register(Category, CategoryManager)


class NoteManager(admin.ModelAdmin):
    list_display = ['note_name', 'note_price','note_date_created', 'note_uploader_user']
    list_editable = ['note_price']
    prepopulated_fields = {'note_slug':('note_name',)}
    list_per_page = 30
admin.site.register(Notes, NoteManager)
