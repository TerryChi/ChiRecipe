from django.shortcuts import render

from .models import Cookbook


def index(request):
    cookbooks = Cookbook.objects.all()
    return render(request, 'index.html', locals())

