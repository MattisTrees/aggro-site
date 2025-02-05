from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello World. You are at the main application index!")

def detail(request, question_id):
	return HttpResponse("You're looking for question %s." % question_id)

def results(request, question_id):
	return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
