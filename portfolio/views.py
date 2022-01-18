from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    #this one line of code grabs everything out of the database, turns them into Python objects
    #and then puts them inside of a list.
    return render(request, 'portfolio/home.html', {'projects': projects})
