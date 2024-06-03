from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Posts


# Create your views here.
def first(request):
    html = """
        <h1>salom posts</h1>
        """
    return HttpResponse(html)


class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'posts'
