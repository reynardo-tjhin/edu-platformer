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

    return render(request, "platformer/index.html")