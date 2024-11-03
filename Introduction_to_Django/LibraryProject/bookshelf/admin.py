from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

# Customize The Admin Interface
class BookAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

# List filters and search capabilities for enhanced admin usability
class BookAdmin(admin.ModelAdmin):
    search_fields= ('title', 'author')

class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_year',)
 