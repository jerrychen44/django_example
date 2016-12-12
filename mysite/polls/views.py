from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Question

from django.template import loader


def index(request):
    #print("test")
    #ver1
    #return HttpResponse("Hello, world. You're at the polls index.")

    #ver2
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    #ver3
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

    #ver4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #ver1
    #return HttpResponse("You're looking at question %s." % question_id)

    #ver2
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# ex: http://127.0.0.1:8000/polls/5/results/
# detail(request=<HttpRequest object>, question_id='5')
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
