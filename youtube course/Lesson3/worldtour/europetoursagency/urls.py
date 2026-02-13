from django.urls import path
from . import views

# Lista patternow URL
urlpatterns = [
    path("", views.index)
]
