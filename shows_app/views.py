from django.shortcuts import render , redirect
from .models import *


def base(request):
    return redirect('/shows')
def index(request):
    show = Show.objects.all()
    if request.method == 'GET':
        contexto = {
                'titulo' : 'All Shows',
                'show' :  show
            }
        return render(request, 'shows_app/index.html' , contexto)
    if request.method == 'POST':
        
        print(request.POST)
        
        return redirect('/')

def shows(request , id):
    if request.method == 'GET':
        contexto = {
            'titulo'  : 'Information About Show',
            'show' : Show.objects.get(id = id),
        }
        return render(request, 'shows_app/shows.html', contexto)

def new(request):
    if request.method == 'GET':
        contexto = {
            'titulo' : 'New Program'
        }
        return render(request, 'shows_app/new.html', contexto)

    if request.method == 'POST':
        print(request.POST)
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            description = request.POST['description'],
            release_date = request.POST['release_date']
            )
        return redirect(f'/shows/{show.id}')

def edit(request, id):
    show = Show.objects.get(id = id)
    if request.method == 'GET':
        contexto = {
            'titulo' : f'Edit Show {show.id}',
            'show' : show
        }
        return render(request , 'shows_app/edit.html', contexto)
    
    if request.method == 'POST':
        print(request.POST , 'este es el post')
        showActualizado = Show.objects.get(id = id)
        showActualizado.title = request.POST['title']
        showActualizado.network = request.POST['network']
        showActualizado.description = request.POST['description']
        showActualizado.release_date = request.POST['release_date'] 
        showActualizado.save()
        return redirect(f'/shows/{showActualizado.id}')

def delete(request , id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect('/')
