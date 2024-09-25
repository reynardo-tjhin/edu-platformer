import uuid

from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponse,
    HttpRequest,
    HttpResponseRedirect,
)
from django.contrib.auth import authenticate, login, logout
from .models import Player

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    The homepage of the game.
    """
    # user already logged in
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse("player:dashboard"))
    
    # user has not logged in
    return render(request, "player/home.html", {})

def login_pageview(request: HttpRequest) -> HttpResponse:
    """
    Player logging in.
    """
    # user already logged in
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse("player:dashboard"))
    
    # user has not logged in
    return render(request, "player/login.html", {})

def create_account_pageview(request: HttpRequest) -> HttpResponse:
    """
    Load the create account page.
    """
    # user already logged in
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse("player:dashboard"))
    
    # user has not logged in
    return render(request, "player/create_account.html", {})

def create_guest_page(request: HttpRequest) -> HttpResponse:
    """
    Create a player with a random ID and save to database.
    """
    # create new player (random)
    username = "player-" + str(uuid.uuid4())[24:] # get the last 12 letters
    password = str(uuid.uuid4()) # generate random id as the password
    new_player = Player(
        username=username,
        current_level=1,
    )
    new_player.set_password(password)
    new_player.save()

    # automatically login the player
    login(request, new_player)
    return HttpResponseRedirect(reverse("player:dashboard"))

def dashboard(request: HttpRequest) -> HttpResponse:
    """
    Player's dashboard.
    """
    # not logged in
    if (not request.user.is_authenticated):
        return HttpResponseRedirect(reverse("player:home"))

    context = {
        "name": request.user.get_username(),
    }
    return render(request, "player/dashboard.html", context)

def logout_page(request: HttpRequest) -> HttpResponse:
    """
    Logout the player.
    """
    logout(request=request)
    return HttpResponseRedirect(reverse("player:home"))



###################################################################
############################# BACKEND #############################
###################################################################

def check_account(request: HttpRequest) -> HttpResponse:
    """
    Check user's name and password.
    """
    user = authenticate(
        request=request,
        username=request.POST.get("name"),
        password=request.POST.get("password"),
    )
    # invalid password or name
    if (user == None):
        context = {
            "login_error_message": "Your password or name is invalid.",
        }
        return render(request, "player/home.html", context)
    # login
    login(
        request=request,
        user=user,
    )
    # upon success
    return HttpResponseRedirect(reverse("player:dashboard"))

def create_account(request: HttpRequest) -> HttpResponse:
    """
    Checks the correctness of inputs and create account.
    """
    name = request.POST.get("name")
    # case 1: check if name already exists
    player = Player.objects.filter(username=name)
    if player:
        print("Error: player's name already exist!")
        context = {
            "create_account_error_message": "This player's name has been taken T^T",
        }
        return render(request, "player/home.html", context)

    # case 2: check if password is empty
    if (request.POST.get("password") == "" or request.POST.get("password2") == ""): 
        print("Error: passwords empty!")
        context = {
            "create_account_error_message": "Please input some passwords *shy*",
        }
        return render(request, "player/home.html", context)

    # case 3: check if passwords match
    if (not (request.POST.get("password") == request.POST.get("password2"))):
        print("Error: passwords differ!")
        context = {
            "create_account_error_message": "Passwords differ...",
        }
        return render(request, "player/home.html", context)
    
    # create new player object
    current_level = 0
    new_player = Player(
        username=name,
        current_level=current_level,
    )
    new_player.set_password(request.POST.get("password"))
    new_player.save()
    print("Success: new player created!")

    # login in the new player immediately
    login(
        request=request,
        user=new_player,
    )

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a 
    # user hits the Back button.
    return HttpResponseRedirect(reverse("player:dashboard"))
