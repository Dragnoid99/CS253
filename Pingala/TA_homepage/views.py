from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>This is homepage for TA</h3> <h1>Frekin' did it!</h1>")