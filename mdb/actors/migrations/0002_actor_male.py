# Generated by Django 2.2.7 on 2019-11-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='male',
            field=models.BooleanField(default=True),
        ),
    ]
