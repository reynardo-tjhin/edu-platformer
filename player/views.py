from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    The homepage of the game.
    """
    context = {}
    return render(request, "player/home.html", context)

def login(request: HttpRequest) -> HttpResponse:
    """
    Player logging in.
    """
    context = {}
    return render(request, "player/login.html", context)