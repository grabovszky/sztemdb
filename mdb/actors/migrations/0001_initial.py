# Generated by Django 2.2.7 on 2019-11-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
