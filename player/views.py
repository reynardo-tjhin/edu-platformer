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