from django.shortcuts import render , redirect


def base(request):
    return redirect('/shows')


def index(request):
    contexto = {
        'titulo' : 'All Shows'
    }
    if request.method == 'POST':
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'shows_app/index.html' , contexto)
