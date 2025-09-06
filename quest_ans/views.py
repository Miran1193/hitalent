from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

# Create your views here.
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreate(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        try:
            question = Question.objects.get(pk=self.kwargs['pk'])
        except Question.DoesNotExist:
            raise NotFound('Question not found')

        serializer.save(question=question)


class AnswerDetail(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
