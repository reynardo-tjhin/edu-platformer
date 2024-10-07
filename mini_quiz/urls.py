from django.urls import path
from . import views

app_name = "mini_quiz"
urlpatterns = [
    # the "table of contents" of mini quiz
    path("", views.index, name="index"),

    # the page where the user needs to click the button to start the quiz
    # to save the time the user starts the quiz
    # preventing tampering of "timer"
    path("<int:quiz_id>/start/", views.start_quiz, name="start_quiz"),

    # the page where the user finishes the quiz successfully/failed
    path("<int:quiz_id>/end/", views.end_quiz, name="end-quiz"),

    # the page between the START QUIZ information page to the QUIZ page
    path("<int:quiz_id>/save-start-time", views.redirect_from_start_to_quiz, name="redirect-from-start-to-quiz"),

    # the quiz page
    # paginator looks like http://127.0.0.1:8000/mini_quiz/1/?page=2
    path("<int:quiz_id>/", views.quiz, name="quiz"),

    # checking the answer of the user
    # example path: http://127.0.0.1:8000/mini_quiz/1/1/1/
    path("<int:quiz_id>/<int:question_id>/<int:answer_id>/check-answer/", views.check_answer, name="check-answer"),
]