from django.shortcuts import render

from .models import Photographer


def about(request):
    photographer_list = Photographer.objects.order_by('id')[:1]
    context = {'photographer_list': photographer_list}
    return render(request, 'about/about.html', context)