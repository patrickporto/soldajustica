from django.shortcuts import (
    render,
    get_object_or_404,
)
from gallery.models import Gallery
from ministry.models import Ministry
from project.models import Project
from blog.models import Post
from .models import Slide

def home(request):
    context = {}
    context['carousel'] = Slide.objects.filter(active=True)
    return render(request, 'app/index.html', context)

def contact(request):
    return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')

def projects(request):
    context = {}
    context['projects'] = Project.objects.filter(active=True)
    return render(request, 'app/projects.html', context)

def get_involved(request):
    return render(request, 'app/get_involved.html')

def donate(request):
    return render(request, 'app/donate.html')

def news_list(request):
    context = {}
    context['posts'] = Post.objects.filter(published=True)
    return render(request, 'app/news/list.html', context)

def news_details(request, slug):
    context = {}
    context['post'] = get_object_or_404(Post, slug=slug)
    return render(request, 'app/news/details.html', context)

def ministries_list(request):
    context = {}
    context['ministries'] = Ministry.objects.all()
    return render(request, 'app/ministries/list.html', context)

def ministries_details(request, slug):
    context = {}
    context['ministry'] = get_object_or_404(Ministry, slug=slug)
    return render(request, 'app/ministries/details.html', context)

def galleries(request):
    context = {}
    context['galleries'] = Gallery.objects.all()
    return render(request, 'app/galleries.html', context)