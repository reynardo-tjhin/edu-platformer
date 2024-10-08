import datetime

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import (
    HttpRequest, 
    HttpResponseRedirect,
    HttpResponse,
)
from django.core.paginator import Paginator
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import MiniQuiz, Question, Answer, PlayerAnswers, PlayerDoes
from player.models import Player

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Show a list of mini quizzes.
    """
    # check if authenticated
    if (not request.user.is_authenticated):
        return render(request, "player/home.html")

    # get the current level of the player
    current_level = request.user.current_level

    # get a list of mini quizzes until the (current level - 1)
    list_of_mini_quizzes = MiniQuiz.objects.order_by("level")
    available_past_quizzes = []
    for mini_quiz in list_of_mini_quizzes:
        if (mini_quiz.level <= current_level - 1):
            available_past_quizzes.append(mini_quiz)

    context = {
        "list_of_mini_quizzes": available_past_quizzes,
    }
    return render(request, "mini_quiz/index.html", context)

def start_quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    To show the start button and to store the start time.
    """
    # check if authenticated
    if (not request.user.is_authenticated):
        return render(request, "player/home.html")

    context = {
        "quiz_id": quiz_id,
    }
    return render(request, "mini_quiz/start_quiz.html", context)

def end_quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    Shows the end of the quiz.
    """
    # check if authenticated
    if (not request.user.is_authenticated):
        return render(request, "player/home.html")

    # quiz successfully completed
    attempts = PlayerDoes.objects.filter(username=request.user.id, quiz_id=quiz_id)
    last_attempt = attempts[attempts.count() - 1]
    if (last_attempt.status):
        message = "Successfully Completed Quiz " + str(quiz_id)
    else:
        message = "Failed to Complete Quiz " + str(quiz_id)

    return render(request, "./mini_quiz/end_quiz.html", {"message": message})

def quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    List the questions and corresponding answers.
    """
    # check if authenticated
    if (not request.user.is_authenticated):
        return render(request, "player/home.html")

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
        "quiz_id": quiz_id,
        "level": mini_quiz.level,
        "page_obj": page_obj,
    }
    return render(request, "./mini_quiz/quiz.html", context)



###################################################################
############################# BACKEND #############################
###################################################################

def redirect_from_start_to_quiz(request: HttpRequest, quiz_id: int) -> HttpResponse:
    """
    When the user presses the 'START QUIZ' button,
    the server will go to this link to create an attempt (to save the start time)
    then redirected to the quiz html.
    """
    # get the current time
    time_start = timezone.now()

    # get quiz object
    try:
        mn_quiz = MiniQuiz.objects.get(pk=quiz_id)
        time_limit = mn_quiz.time_limit # in seconds
    except (ObjectDoesNotExist):
        return render(request, "mini_quiz/to_be_completed.html")

    # create a new attempt
    attempts = PlayerDoes.objects.filter(username=request.user.id, quiz_id=quiz_id)
    new_attempt = PlayerDoes(
        username=request.user,
        quiz_id=MiniQuiz.objects.get(pk=quiz_id),
        attempt_id=attempts.count()+1,
        status=False,
        start_time=time_start,
        end_time=time_start+datetime.timedelta(seconds=time_limit),
    )
    new_attempt.save()
    print("New Attempt created!")
    return HttpResponseRedirect(reverse("mini_quiz:quiz", args=(quiz_id,)))

def check_answer(request: HttpRequest, quiz_id: int, question_id: int, answer_id: int) -> HttpResponse:
    """
    Check the answer based on the question and answer.
    """
    # create the variables to store the data
    time_answered = timezone.now()

    # check if the answer is correct
    selected_answer = Answer.objects.get(pk=answer_id)
    is_correct = selected_answer.is_correct_answer

    # create the data to store in the 'PlayerAnswers' table
    new_answer = PlayerAnswers(
        username=request.user,
        question_id=Question.objects.get(pk=question_id),
        is_correct=is_correct,
        time_answered=time_answered,
    )
    new_answer.save()
    print("New Player's Answer created!")

    # answer is correct -> go to the next question
    if (is_correct):
        
        # check the last page
        # the user has completed the mini-quiz
        if (request.GET['page'] == request.GET['num_pages']):

            # update the status
            attempts = PlayerDoes.objects.filter(username=request.user.id, quiz_id=quiz_id)            
            last_attempt = attempts[attempts.count()-1]
            last_attempt.status = True
            last_attempt.save()
            print("Player successfully completes the quiz!")

            # update the player's level
            player = Player.objects.get(username=request.user.username)
            quiz = MiniQuiz.objects.get(quiz_id=quiz_id)
            player.current_level = max(player.current_level, quiz.level + 1)
            player.save()
            print("Player's level successfully increases!")

            # return to the player's dashboard
            return HttpResponseRedirect(reverse("mini_quiz:end-quiz", args=(quiz_id,)))

        resultant_url = reverse("mini_quiz:quiz", args=(quiz_id,))
        if 'page' in request.GET:
            resultant_url += f"?page={int(request.GET['page']) + 1}"
        return HttpResponseRedirect(resultant_url)

    # retry & refresh the current page
    resultant_url = reverse("mini_quiz:quiz", args=(quiz_id,))
    if 'page' in request.GET:
        resultant_url += f"?page={request.GET['page']}"
        resultant_url += f"&message=incorrect"
        resultant_url += f"&answer_id={answer_id}"
    return HttpResponseRedirect(resultant_url)