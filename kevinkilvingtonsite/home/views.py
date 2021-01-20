from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture


def home(request):
    return HttpResponse("This is the home page")