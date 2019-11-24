from django.contrib import admin
from .models import Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Genre, GenreAdmin)

# Register your models here.
