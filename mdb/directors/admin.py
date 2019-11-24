from django.contrib import admin
from .models import Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'male', 'birth_date')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'male')
    search_fields = ('first_name', 'last_name', 'male', 'birth_date')
    list_per_page = 25

admin.site.register(Director, DirectorAdmin)
