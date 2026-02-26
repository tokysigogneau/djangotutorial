import datetime

from django.contrib import admin  # type: ignore

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ["choice_text"]
    list_filter = ["votes"]
    ordering = ["votes"]
    search_fields = ["foreign_key__related_fieldname"]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoicesAdmin)
