from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages


def base(request):
    return redirect('/shows')

def index(request):
    show = Show.objects.all()
    if request.method == 'GET':
        contexto = {
                'titulo' : 'All Shows',
                'show' :  show,
            }
        return render(request, 'shows_app/index.html' , contexto)
    
    if request.method == 'POST':
        print(request.POST)
        # este esta echo por el link que ejecuta el form
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

        # validador
        errores = Show.objects.validacion(request.POST)

        if len(errores) > 0:
            print(errores)
            for key , value in errores.items():
                messages.warning(request , value)

            request.session['show_form_title'] = request.POST['title']
            request.session['show_form_network'] = request.POST['network']
            request.session['show_form_release_date'] = request.POST['release_date']
            request.session['show_form_description'] = request.POST['description']

            return redirect('/shows/new')

        else:
            print(request.POST)
            request.session['show_form_title'] = ''
            request.session['show_form_network'] = ''
            request.session['show_form_description'] = ''
            request.session['show_form_release_date'] = ''
            
            show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'],
            )
            mensajeExito = f'exito al agregar el Show {show.title}'
            messages.success(request, mensajeExito)
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
        
        # validador
        errores = Show.objects.validacion(request.POST)
        if len(errores) > 0:
            print(errores)
            for key , value in errores.items():
                messages.warning(request , value)

            request.session['show_form_title'] = request.POST['title']
            request.session['show_form_network'] = request.POST['network']
            request.session['show_form_release_date'] = request.POST['release_date']
            request.session['show_form_description'] = request.POST['description']

            return redirect(f'/shows/{show.id}/edit')
        else:
            print(request.POST)
            request.session['show_form_title'] = ''
            request.session['show_form_network'] = ''
            request.session['show_form_description'] = ''
            request.session['show_form_release_date'] = ''

            print(request.POST , 'este es el post')
            show = Show.objects.get(id = id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.description = request.POST['description']
            show.release_date = request.POST['release_date'] 
            show.save()
            return redirect(f'/shows/{show.id}')

def delete(request , id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect('/')
