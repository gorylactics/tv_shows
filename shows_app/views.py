from django.shortcuts import render , redirect


def base(request):
    return redirect('/shows')


def index(request):
    contexto = {
        'titulo' : 'All Shows'
    }
    return render(request, 'shows_app/index.html' , contexto)
