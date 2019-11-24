from django.db import models
from datetime import date
from directors.models import Director
from genres.models import Genre
from actors.models import Actor

class Movie(models.Model):
    films_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    running_time = models.IntegerField()
    release_date = models.DateField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Starring(models.Model):
    film_id = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    actor_id = models.ForeignKey(Actor, on_delete=models.DO_NOTHING)
    character_name = models.CharField(default="random character", max_length=200)

    def __str__(self):
        return self.character_name
