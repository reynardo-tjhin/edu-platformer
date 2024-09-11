from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
)

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # not logged in
    if (not request.user.is_authenticated):
        return HttpResponseRedirect(reverse("player:home"))
    
    # the player's current level can be found in request
    return render(request, "platformer/index.html")