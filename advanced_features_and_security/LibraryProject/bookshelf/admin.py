from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomUserAdmin
from django.contrib.auth import get_user_model

# Register your model
admin.site.register(CustomUser, CustomUserAdmin)

# Customize The Admin Interface
class BookAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'publication_year')


# List filters and search capabilities for enhanced admin usability
class BookAdmin(admin.ModelAdmin):
    search_fields= ('title', 'author')

class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_year',)



# Customize the admin interface
class CustomeUserAdmin(admin.ModelAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )


