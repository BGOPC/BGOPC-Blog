from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception):
    return render(request, '404.html', status=404)