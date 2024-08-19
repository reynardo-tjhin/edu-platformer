from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import (
    HttpRequest, 
    HttpResponseRedirect,
    HttpResponse,
)
from django.core.paginator import Paginator

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

def start_quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    To show the start button and to store the start time.
    """
    context = {
        "quiz_id": quiz_id,
    }
    return render(request, "mini_quiz/start_quiz.html", context)

def quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    List the questions and corresponding answers.
    """
    # get the mini quiz object based on the quiz_id
    mini_quiz = get_object_or_404(MiniQuiz, pk=quiz_id)        
    
    # get the question and corresponding answers list
    question_list = mini_quiz.question_set.all()
    question_and_answers = []
    for question in question_list:
        question_and_answers.append({
            "question": question,
            "answers": question.answer_set.all(),
        })
    
    # create paginator
    paginator = Paginator(question_and_answers, 1) # show 1 question per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "./mini_quiz/quiz.html", context)


def check_answer(request: HttpRequest, question_id: int, answer_id: int) -> HttpResponse:
    """
    Check the answer based on the question and answer.
    """
    # get the selected answer
    selected_answer = get_object_or_404(Answer, pk=answer_id)
    
    # the selected answer is correct
    if (selected_answer.is_correct_answer):
        return HttpResponseRedirect(reverse())
    # selected answer is incorrect
    else:
        pass