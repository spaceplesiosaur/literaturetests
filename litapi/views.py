from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SourceSerializer, CharacterSerializer, QuizSerializer, CharacterDescriptionSerializer, QuestionSerializer, AnswerSerializer
from .models import Source, Character, Quiz, CharacterDescription, Question, Answer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('title')
    serializer_class = SourceSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name')
    serializer_class = CharacterSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('title')
    serializer_class = QuizSerializer

class CharacterDescriptionViewSet(viewsets.ModelViewSet):
    queryset = CharacterDescription.objects.all().order_by('body')
    serializer_class = CharacterDescriptionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('body')
    serializer_class = SourceSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('body')
    serializer_class = AnswerSerializer
