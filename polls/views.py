from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

#function index is a route handler
def index(request):
    latest_quest_list = Question.objects.order_by('- pub_date')[:5]
    template = loader.loader. get_template('polls/index.html') 
    context = {'latest_quest_list': latest_quest_list}
    return render(request,'polls/index.html', context)
    
    # ex: /details/5/
def detail(request, question_id):
    return HttpResponse("You're looking at result of question %s." % question_id)

    # ex: /polls/5/result/
def results(request, question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)
    
    # ex: /polls/5/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)