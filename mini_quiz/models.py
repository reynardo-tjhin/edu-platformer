from django.db import models

# Create your models here.
class MiniQuiz(models.Model):
    
    # the primary key to uniquely identify each quiz
    quiz_id = models.IntegerField(primary_key=True)

    # the other attributes
    level = models.IntegerField()
    genre = models.CharField(max_length=50) # may be used in the future
    summary = models.CharField(max_length=500) # summarises the learnings of the mini quiz

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