import permissions
from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Posts,Comments
from .serializers import PostSerializer,PostDetailSerializer,CommentsSerializer
from rest_framework.response import Response
from rest_framework import filters
# Create your views here.

class ListCreatePost(generics.ListCreateAPIView):
    serializer_class = PostDetailSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['Author','Title','Tags']#Search filter not working,throwing error of unknown fields even on searching through the right fields
    ordering_fields = ['Author','Title','Date_Added','Date_Edited','Tags']
    def perform_create(self, serializer):
        serializer.save(Author = self.request.user)

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    def retrieve(self, request,pk):
        queryset = self.get_object()
        serializer = PostDetailSerializer(queryset,many = False)
        return Response(serializer.data)

class UserPosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['Title','Tags']
    def perform_create(self, serializer):
        serializer.save(Author = self.request.user)
    def get_queryset(self):
        return Posts.objects.filter(Author_id = self.request.user.id) 

class Comm_ents(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('pk'))
    def perform_create(self, serializer):
        POSTID = self.kwargs.get('pk')
        serializer.save(Author=self.request.user,post_id = POSTID)
   