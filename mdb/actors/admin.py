from django.contrib import admin
from .models import Actor

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'male', 'birth_date')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'male')
    search_fields = ('first_name', 'last_name', 'male', 'birth_date')
    list_per_page = 25


admin.site.register(Actor, ActorAdmin)
