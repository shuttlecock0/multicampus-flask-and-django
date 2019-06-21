from django.shortcuts import render, redirect
from .models import Genre, Movie, Score
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    scores = movie.score_set.order_by('-pk')
    context = {
        'movie': movie,
        'genre': genre,
        'scores': scores,
    }
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        context = {
            'movie': movie,
        }
        return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def scores_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        score = request.POST.get('score')
        maked_score = Score(movie=movie, content=content, score=score)
        maked_score.save()
        return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)

def scores_delete(request, movie_pk, score_pk):
    score = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        score.delete()
    return redirect('movies:detail', movie_pk)
