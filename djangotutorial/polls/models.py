import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.db.models import Sum, Avg
from django.utils.html import format_html

MAX_LENGTH = 20

def text_excerpt(text, max_length):
 return text[:max_length] + ('...' if len(text) > max_length
else '')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "{} {}".format(self.pub_date,
                              text_excerpt(self.question_text,
                                           MAX_LENGTH))

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def age(self):
        return timezone.now() - self.pub_date

    def get_choices(self):
        resultat = self.choice_set.aggregate(total=Sum('votes'))
        total = resultat['total']

        if total > 0 :
            return [(c.choice_text, c.votes, c.votes / total * 100)
                    for c in self.choice_set.all()]
        else :
            return [(c.choice_text, 0, 0)
                    for c in self.choice_set.all()]


    def get_max_choice(self):
        choices = self.choice_set.all()
        resultat = self.choice_set.aggregate(total=Sum('votes'))
        total = resultat['total']
        max_choice = max(choices, key=lambda c: c.votes / total)
        return (max_choice.choice_text, max_choice.votes / total)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return text_excerpt(self.choice_text, MAX_LENGTH)

    def votes_repartition (self, primary_key):
        q = Question.objects.get(pk=primary_key)
        #nb_of_questions = q.choice_set.all().count()
        total_votes = 0
        repartition_list = []

        for choice in q.choice_set.all():
            total_votes += choice.votes

        for choice in q.choice_set.all():
            if total_votes >0:
                repartition_list.append(choice.votes / total_votes * 100)
            else:
                print("le total de vote est à 0")


        return repartition_list
