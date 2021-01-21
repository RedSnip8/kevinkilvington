from django.shortcuts import render

from .models import Picture


def home(request):
    latest_photos_list = Picture.objects.order_by('id')[:25]
    context = {'latest_photos_list': latest_photos_list}
    return render(request, 'home/home.html', context)