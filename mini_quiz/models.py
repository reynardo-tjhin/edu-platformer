from django.db import models

from player.models import Player

# Create your models here.
class MiniQuiz(models.Model):
    
    # the primary key to uniquely identify each quiz
    quiz_id = models.IntegerField(primary_key=True)

    # the other attributes
    level = models.IntegerField()
    genre = models.CharField(max_length=50) # may be used in the future
    summary = models.CharField(max_length=500) # summarises the learnings of the mini quiz
    time_limit = models.IntegerField(default=30)

    def __str__(self) -> str:
        return f"Mini Quiz Level {self.level}"

class Question(models.Model):

    # the primary key to uniquely identify each question
    question_id = models.IntegerField(primary_key=True)

    # the other attributes
    question_text = models.CharField(max_length=200)
    quiz_id = models.ForeignKey(MiniQuiz, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.question_text}"

class Answer(models.Model):

    # the primary key to uniquely identify each answer
    answer_id = models.IntegerField(primary_key=True)

    # the other attributes
    mini_quiz_id = models.ForeignKey(MiniQuiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct_answer = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.answer_text}"


# RELATIONSHIP MODELS
class PlayerAnswers(models.Model):
    """
    This is a relationship between 'Player' and 'Quiz' models.
    Player 'answers' the quiz question without knowing which answer the player selected.
    """
    username = models.ForeignKey(Player, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    is_correct = models.BooleanField()
    time_answered = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.username} is attempting {self.question_id}"
    
class PlayerDoes(models.Model):
    """
    This is a relationship between 'Player' and 'MiniQuiz' models.
    Player 'completes' the quiz after answer everything correctly and within time.
    """
    username = models.ForeignKey(Player, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(MiniQuiz, on_delete=models.CASCADE)

    attempt_id = models.IntegerField(default=0) # to uniquely identify which attempt
    status = models.BooleanField() # 0 indicates failed, 1 indicates completed
    start_time = models.DateTimeField() # the time the player clicks on the "start" button
    end_time = models.DateTimeField(null=True) # the time the player needs to complete


    def __str__(self) -> str:
        return f"[Attempt {self.attempt_id}]: {self.username} does {self.quiz_id}"