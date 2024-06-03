from django.urls import path
from .views import first, HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='first'),
]