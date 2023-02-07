from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Question
from user.models import User
from .serializers import QuestionListSerializer,QuestionDetailsSerializer
# Create your views here.

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
 
class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionDetailsSerializer
       

