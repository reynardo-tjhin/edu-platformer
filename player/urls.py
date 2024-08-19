from django.urls import path
from . import views

app_name = "player"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("create-account/", views.create_account_pageview, name="create-account"),
    path("check-new-account/", views.create_account, name="check-new-account"),
    path("<str:name>/dashboard/", views.dashboard, name="dashboard"),
]