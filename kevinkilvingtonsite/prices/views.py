from django.shortcuts import render

from .models import Services


def prices(request):
    services_list = Services.objects.order_by('id')[:10]
    context = {'services_list': services_list}
    return render(request, 'prices/prices.html', context)