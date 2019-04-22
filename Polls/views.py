from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from .models import Questions


def pollsIndex(request):
    questions = Questions.objects.order_by('-published_date')
    context = {'questions': questions}
    return render(request, 'Polls/index.html', context)


def details(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    context = {'question': question}
    return render(request, 'Polls/details.html', context)


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    context = {'question': question}
    return render(request, 'Polls/results.html', context)


def votes(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
    except:
        context = {'question': question, 'error_message': 'Please select a choice!'}
        return render(request, 'Polls/details.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse('<div style="background-color: #2980b9; overflow: hidden;"><br><br><br><br><h1 style="text-align: center; font-size: 36px; color: white; ">Thank you for the vote!</h1><br><br><br><br><br><p style="text-align: center; font-size: 32px; color: white;">Have a nice day!</p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></div>')
