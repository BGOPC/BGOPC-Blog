from django.template import loader
from django.http import HttpResponseNotFound


def handler404(request, exception):
    content = loader.render_to_string('404.html', {}, request)
    return HttpResponseNotFound(content)