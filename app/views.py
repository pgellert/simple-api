from django.http import HttpResponse
from django.shortcuts import render


GITHUB_README_URL = 'https://raw.githubusercontent.com/pgellert/simple-api/master/README.md'  # noqa: E501


def index(request):
    return render(request, "index.html")
    # with urllib.request.urlopen(GITHUB_README_URL) as response:
    #     content = response.read().decode('utf-8')
    #     return HttpResponse(markdown2.markdown(content))


def grocery_list(request):
    return HttpResponse("Hello! This is the URI for the grocery list")


def grocery_by_name(request, name):
    return HttpResponse("Hello! This is the URI for the " + name)
