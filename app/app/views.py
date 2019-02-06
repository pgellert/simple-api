from django.http import HttpResponse
import urllib
import markdown
import os

def index(request):
    with urllib.request.urlopen('https://raw.githubusercontent.com/pgellert/simple-api/master/README.md') as response:
        content = response.read()
        return HttpResponse(markdown.markdown(content))

def grocery_list(request):
    return HttpResponse("Hello! This is the URI for the grocery list")

def grocery_by_name(request, name):
    return HttpResponse("Hello! This is the URI for the " + name)
