from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import (
    HttpRequest, 
    HttpResponseRedirect,
    HttpResponse,
)

from .models import MiniQuiz, Answer

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Show a list of mini quizzes.
    """
    list_of_mini_quizzes = MiniQuiz.objects.order_by("level")
    context = {
        "list_of_mini_quizzes": list_of_mini_quizzes,
    }
    return render(request, "mini_quiz/index.html", context)

def quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    List the questions and corresponding answers.
    """
    # get the mini quiz
    mini_quiz = get_object_or_404(MiniQuiz, pk=quiz_id)
    # create a "JSON" data
    context = {
        "level": mini_quiz.level,
        "questions": [],
    }
    # add the questions and answers
    for i, question in enumerate(mini_quiz.question_set.all()):
        # question has a question text and answer texts
        context["questions"].append({})
        context["questions"][i]["question"] = question
        context["questions"][i]["answers"] = []
        # add the answers
        for answer in question.answer_set.all():
            context["questions"][i][f"answers"].append(answer)
    # render the html file
    return render(request, "mini_quiz/quiz.html", context)

def check_answer(request: HttpRequest, question_id: int, answer_id: int) -> HttpResponse:
    """
    Check the answer based on the question and answer.
    """
    # get the selected answer
    selected_answer = get_object_or_404(Answer, pk=answer_id)
    
    # the selected answer is correct
    if (selected_answer.is_correct_answer):
        return HttpResponseRedirect(request, )
    # selected answer is incorrect
    else:
        pass