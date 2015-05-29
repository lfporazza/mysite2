from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Ola a todos</h1>")

def detail(request, question_id):
    return HttpResponse ("You ' re looking at the results of question %s."% question_id)

def results(request,question_id):
    response="You ' re looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You ' re voting on question %s." % question_id)







def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html',context)
