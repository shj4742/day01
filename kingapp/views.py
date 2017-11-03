from django.shortcuts import render

# Create your views here.

from .models import HeroInfo
def image(request, id):
    return render(request, 'image.html')


def index(request):
    herolist = HeroInfo.objects.all()
    context = {'herolist': herolist}
    return render(request, 'index.html', context)


def detail(request, id):
    hero = HeroInfo.objects.get(pk=id)
    context = {'hero': hero}
    return render(request, 'detail.html', context)
