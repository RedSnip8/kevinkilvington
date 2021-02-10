from django.shortcuts import render, get_list_or_404

from .models import Album
from home.models import Picture


def albums(request):
    cover_photo = Picture.objects.filter(on_grid=True).select_related('photo_album').distinct("photo_album").order_by("photo_album", "-id")

    context = { "cover_photo": cover_photo }

    return render(request, 'albums/albums.html', context)

def album(request, album_id):
    album_selected = get_list_or_404(Album, pk=album_id)
    context = {"album_selected": album_selected}

    return render(request, 'albums/album.html', context)
