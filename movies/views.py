from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'index.html',context)