from django.contrib import admin
from .models import Movie, Starring

class MovieAdmin(admin.ModelAdmin):
    list_display = ('films_id', 'title', 'running_time', 'release_date', 'director', 'genre')
    list_display_links = ('title', 'director', 'genre')
    list_filter = ('title', 'director', 'genre')
    search_fields = ('title', 'release_date', 'director', 'genre')
    list_per_page = 25

class StarringAdmin(admin.ModelAdmin):
    list_display = ('film_id', 'actor_id', 'character_name')
    list_display_links = ('film_id', 'actor_id', 'character_name')
    list_filter = ('film_id', 'actor_id', 'character_name')
    search_fields = ('film_id', 'actor_id', 'character_name')
    list_per_page = 25

admin.site.register(Movie, MovieAdmin)
admin.site.register(Starring, StarringAdmin)

# Register your models here.
