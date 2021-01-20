from django.shortcuts import render
from django.http import HttpResponse


def prices(request):
    return HttpResponse("This is the prices page")