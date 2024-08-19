from django.urls import path
from . import views

app_name = "mini_quiz"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:quiz_id>/start/", views.start_quiz, name="start_quiz"),
    path("<int:quiz_id>/", views.quiz, name="quiz"),
    path("<int:question_id>/<int:answer_id>/", views.check_answer, name="check_answer"),
]