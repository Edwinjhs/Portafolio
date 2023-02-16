from django.shortcuts import render
from .models import Project

# Create your views here.

def render_project_home(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects })
