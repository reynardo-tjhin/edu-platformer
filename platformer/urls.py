from django.urls import path

from . import views

app_name = 'platformer'
urlpatterns = [
    path("", views.index, name="index"),
]