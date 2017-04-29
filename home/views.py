from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Stories


def index(request):
    template = loader.get_template('home/index.html')
    latest_feed = Stories.f1
    context = {'latest_feed': latest_feed,}
    return HttpResponse(template.render(context, request))

