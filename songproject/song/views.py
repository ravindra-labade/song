from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song
from django.contrib.auth.decorators import login_required


def add_song(request):
    template_name = 'song/add.html'
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_song(request):
    template_name = 'song/show.html'
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, template_name, context)


def update_song(request, pk):
    template_name = 'song/add.html'
    obj = Song.objects.get(id=pk)
    form = SongForm(instance=obj)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_song(request, pk):
    obj = Song.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'song/confirm.html')