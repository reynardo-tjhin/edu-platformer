from django.contrib import admin

from .models import MiniQuiz, Question, Answer

# Register your models here.
class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
admin.site.register(Question, QuestionAdmin)

class QuestionLinkInLine(admin.TabularInline):
    model = Question
    fieldsets = [
        (None, {"fields": ["question_id", "question_text"]}),
    ]
    show_change_link = True

class MiniQuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["quiz_id", "level", "genre", "summary"]}),
    ]
    inlines = [QuestionLinkInLine]
admin.site.register(MiniQuiz, MiniQuizAdmin)