import datetime

from django.contrib import admin  # type: ignore

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text"]
    list_filter = ["pub_date"]
    ordering = ["pub_date"]
    search_fields = ["foreign_key__related_fieldname"]


class ChoicesAdmin(admin.ModelAdmin):
    list_display = ["choice_text"]
    list_filter = [""]
    ordering = [""]
    search_fields = ["foreign_key__related_fieldname"]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoicesAdmin)
