from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import genre_choices

from .models import Movie


def index(request):
    movies = Movie.objects.order_by('-release_date')

    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)

    context = {
        'movies': paged_movies
    }

    return render(request, 'movies/movies.html', context)


def movie(request, films_id):
  movie = get_object_or_404(Movie, pk=films_id)

  context = {
    'movie': movie
  }

  return render(request, 'movies/movie.html', context)


def search(request):
    queryset_list = Movie.objects.order_by('-release_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    context = {
        'genre_choices': genre_choices,
        'movies': queryset_list,
        'values': request.GET
    }

    return render(request, 'movies/search.html', context)
