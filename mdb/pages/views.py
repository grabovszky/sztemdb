from django.shortcuts import render
from django.http import HttpResponse
from movies.choices import genre_choices

from movies.models import Movie

def index(request):
    movies = Movie.objects.order_by('-release_date')[:3]

    context = {
        'movies': movies,
        'genre_choices': genre_choices
    }

    return render(request, 'pages/index.html', context)
