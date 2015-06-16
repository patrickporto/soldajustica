from django.shortcuts import render
from project.models import Project

def home(request):
    return render(request, 'app/index.html')

def contact(request):
    return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')

def projects(request):
    context = {}
    context['projects'] = Project.objects.filter(active=True)
    return render(request, 'app/projects.html', context)