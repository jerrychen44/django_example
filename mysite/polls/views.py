from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question

def index(request):
    #print("test")
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
# ex: http://127.0.0.1:8000/polls/5/results/
# detail(request=<HttpRequest object>, question_id='5')
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
