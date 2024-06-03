from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first(request):
    html = """
    <h1>salom blog</h1>
    """
    return HttpResponse(html)
