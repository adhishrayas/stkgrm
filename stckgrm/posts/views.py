from django.shortcuts import render
from rest_framework import generics
from stckgrm.permissions.permissions import IsAuthorOrReadOnly
from .models import Question,Answers
from user.models import User
from .serializers import QuestionListSerializer,QuestionDetailsSerializer,CommentSerializer,CommentDetailSerializer
# Create your views here.

class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Answers.objects.all()
    serializer_class = CommentDetailSerializer

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def get_queryset(self):
        return Answers.objects.filter(title = self.post)
    

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
 
class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionDetailsSerializer
       

