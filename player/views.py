import hashlib
import hmac
import uuid

from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponse,
    HttpRequest,
    HttpResponseRedirect,
)
from .models import Player

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

def create_account_pageview(request: HttpRequest) -> HttpResponse:
    """
    Load the create account page.
    """
    context = {}
    return render(request, "player/create_account.html", context)

def create_account(request: HttpRequest) -> HttpResponse:
    """
    Create account.
    """
    print("got here!")

    name = request.POST.get("name")
    # case 1: check if name already exists
    player = Player.objects.filter(name=name)
    if player:
        print("Error: player's name already exist!")
        context = {
            "error_message": "This player's name has been taken T^T",
        }
        return render(request, "player/create_account.html", context)

    # case 2: check if passwords match
    password = hashlib.sha256(request.POST.get("password").encode('utf-8')).hexdigest()
    password2 = hashlib.sha256(request.POST.get("password2").encode('utf-8')).hexdigest()
    if (not hmac.compare_digest(password, password2)):
        print("Error: passwords differ!")
        context = {
            "error_message": "Passwords differ...",
        }
        return render(request, "player/create_account.html", context)
    
    # get player's unique ID
    player_id = uuid.uuid4()
    # to be safe: check a unique uuid
    player = Player.objects.filter(player_id=player_id)
    while (player):
        player_id = uuid.uuid4()
        player = Player.objects.filter(player_id=player_id)

    # create new player object
    current_level = 0
    new_player = Player(
        player_id=player_id,
        name=name,
        password=password,
        current_level=current_level,
    )
    new_player.save()
    print("Success: new player created!")

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a 
    # user hits the Back button.
    return HttpResponseRedirect(reverse("player:dashboard", args=(name,)))


def dashboard(request: HttpRequest, name: str) -> HttpResponse:
    """
    Player's dashboard.
    """
    context = {
        "name": name,
    }
    return render(request, "player/dashboard.html", context)