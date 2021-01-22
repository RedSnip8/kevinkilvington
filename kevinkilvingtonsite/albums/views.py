from django.shortcuts import render, get_list_or_404

from .models import Album


def albums(request):
    albums_list = Album.objects.filter(is_active=True)
    context = {"albums_list": albums_list}

    return render(request, 'albums/albums.html', context)

def album(request, album_id):
    album_selected = get_list_or_404(Album, pk=album_id)
    context = {"album_selected": album_selected}

    return render(request, 'albums/album.html', context)
