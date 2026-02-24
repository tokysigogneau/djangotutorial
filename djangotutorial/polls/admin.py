import datetime

from django.contrib import admin  # type: ignore

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text"]
    list_filter = [datetime.datetime(2026,2,24)]

    @admin.display(empty_value="???")
    def view_question(self, obj):
        return  obj.question_text

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ["choice_text"]

    @admin.display(empty_value="???")
    def view_choices(self, obj):
        return obj.choice_text

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoicesAdmin)
