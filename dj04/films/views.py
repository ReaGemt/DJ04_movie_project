from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from .models import Film
from django.db import models

def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')
        else:
            print(form.errors)  # Можно временно вывести ошибки в консоль
    else:
        form = FilmForm()
    return render(request, 'films/film_form.html', {'form': form})

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def film_delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('film_list')
    return render(request, 'films/film_confirm_delete.html', {'film': film})
