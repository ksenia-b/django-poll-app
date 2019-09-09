from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from .models import Question

# Get an instance of a logger
logger = logging.getLogger(__name__)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    logger.debug('Something went wrong!')
    return HttpResponse(output)
