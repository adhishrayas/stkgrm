from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionListSerializer,QuestionDetailsSerializer
# Create your views here.

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailsSerializer
       

