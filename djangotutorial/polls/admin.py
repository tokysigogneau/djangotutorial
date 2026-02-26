import datetime

from django.contrib import admin  # type: ignore

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ["choice_text"]
    list_filter = ["votes"]
    ordering = ["votes"]
    search_fields = ["foreign_key__related_fieldname"]



admin.site.register(Question,QuestionAdmin)

