from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
from .models import Choice


# Create your views here.
def index (request):
    question_array =Question.objects.order_by('-pub_date')[:5]

    context = {
        'title' :'Poll Questions',
        'data' : question_array
    }
    return render(request, 'mypoll/index.html',context)


def test (request):
    return HttpResponse('Hello from myPoll APP--TEST VIEW!')


# THE DETAILS PAGE OF A SPECIFIC POLL
def detail(request, question_id):
    try:
        # GETTING THE QUESTION FOR THE PQN
       
        question = get_object_or_404(Question, pk=question_id)
     
        
        
        
    except Question.DoesNotExit:
        raise Http404("Question does not exits")
    context ={
        'question' :question,
       
    }
        
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'mypoll/details.html',context)



def results(request, question_id):
    response ="You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)