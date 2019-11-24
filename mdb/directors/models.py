from django.db import models
from datetime import date

class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    male = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.first_name + " " + self.last_name