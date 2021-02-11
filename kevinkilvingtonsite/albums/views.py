from django.shortcuts import render, get_list_or_404

from .models import Album, Events
from home.models import Picture


def albums(request):
    cover_photo = Picture.objects.filter(on_grid=True, album_cover=True).select_related('photo_album').distinct("photo_album").order_by("photo_album", "-id")

    context = { "cover_photo": cover_photo }

    return render(request, 'albums/albums.html', context)

def events(request, album_id):
    album_selected = Picture.objects.filter(photo_album=album_id).select_related('photo_album', 'event_name').order_by("-id")
    album_name = get_list_or_404(Album, pk=album_id)
    context = {"album_selected": album_selected, 'album_name': album_name}

    return render(request, 'albums/events.html', context)

def event(request, event_id):
    event_selected = Picture.objects.filter(event_name=event_id).select_related('event_name').order_by("id")
    event_name = get_list_or_404(Events, pk=event_id)[:1]
    context = {"event_selected": event_selected, "event_name": event_name}

    return render(request, 'alnums/event.htmls', context)