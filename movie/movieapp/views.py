from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    id = Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'id':id})

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        description = request.POST.get('description')
        image = request.FILES['image']
        movie = Movie(name=name,year=year,description=description,image=image)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect("/")
    return render(request,"delete.html")