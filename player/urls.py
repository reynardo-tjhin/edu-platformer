from django.urls import path
from . import views

app_name = "player"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_pageview, name="login"),
    path("check-account/", views.check_account, name="check-account"),
    path("create-account/", views.create_account_pageview, name="create-account"),
    path("check-new-account/", views.create_account, name="check-new-account"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_page, name="logout"),
]