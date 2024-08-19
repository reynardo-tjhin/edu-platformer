from django.urls import path
from . import views

app_name = "player"
urlpatterns = [
    # the home page: login, play as guest & create new account
    path("", views.home, name="home"),

    # login pages
    path("login/", views.login_pageview, name="login"),
    path("check-account/", views.check_account, name="check-account"),

    # create guest player
    path("create-guest/", views.create_guest_page, name="create-guest"),

    # create new account pages
    path("create-account/", views.create_account_pageview, name="create-account"),
    path("check-new-account/", views.create_account, name="check-new-account"),

    # the player's dashboard once logged in
    path("dashboard/", views.dashboard, name="dashboard"),
    
    # for handling logout
    path("logout/", views.logout_page, name="logout"),
]