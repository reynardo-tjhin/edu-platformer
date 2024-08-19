from django.contrib import admin

from .models import MiniQuiz, Question, Answer

# Register your models here.
class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1

class MiniQuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["level", "genre", "summary"]}),
    ]
    inlines = [QuestionInLine, AnswerInLine]

admin.site.register(MiniQuiz, MiniQuizAdmin)