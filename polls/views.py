from django.shortcuts import render, get_object_or_404

from polls.models import Question
# Create your views here.

def index(request):
	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'lastest_question_list': lastest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)	
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = 'You are looking at the results of question {0}'
	return HttpResponse(response .format(question_id))

def vote(request, question_id):
	return HttpResponse('You are voting on question {0}' .format(question_id))