# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
# from django.template import loader
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:2]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index2GridLayout.html", context)

class IndexView(generic.TemplateView):
    template_name = 'appNR/index.html'


class Link1View(generic.TemplateView):
    template_name = 'appNR/link1.html'
