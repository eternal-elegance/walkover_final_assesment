from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from scores.models import Result

class QuizListView(ListView):
    model = Quiz 
    template_name = 'tests/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'tests/quiz.html', {'obj': quiz})