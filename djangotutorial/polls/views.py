from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import QuestionAddForm

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Question, Choice

NB_MAX_CHOIX = 5

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

class AllQuestionsView(generic.ListView):
    template_name = "polls/all.html"
    context_object_name = "all_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class StatisticView(generic.ListView):
    model = Question
    template_name = "polls/statistics.html"
    context_object_name = "questions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_questions"] = Question.objects.count()
        context["total_choice"] = Choice.objects.count()

        return context

# class StatisticView(generic.StatisticView):
#     model = Question
#     template_name = "polls/statistics.html"
#     total_questions = len(Question.objects.all())
#     context = {"latest_question_list": total_questions}


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def add(request):
 return render(request, 'polls/add.html', {
 'liste_no_choix': range(NB_MAX_CHOIX)
 })


###############################

def confirm_add(request):
    # récupération du libellé de la question,
    # sans les éventuels espaces avant et après
    question_text = request.POST['question_text'].strip()
    if question_text:
        # ajout de la question si elle n'est pas vide
        question = Question(question_text=question_text,
        pub_date=timezone.now())
        question.save()
        # on traite à présent les champs de choix remplis
        # (on s'arrête au premier vide)
        for no_choix in range(NB_MAX_CHOIX):
            nom_champ = 'choix_{}'.format(no_choix)
            choice_text = request.POST[nom_champ].strip()
            if choice_text:
                choice = Choice(question=question,
                choice_text=choice_text)
                choice.save()
            else:
                break
        return render(request, 'polls/confirm_add.html')
    else:
        # réaffichage du formulaire de saisie de la question
        # avec le message d'erreur
        return render(request, 'polls/add.html', {
            'error_message': "You didn't enter a question text",
})
