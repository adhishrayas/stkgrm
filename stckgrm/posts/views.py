import permissions
from django.shortcuts import render
from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer,PostDetailSerializer
from rest_framework.response import Response
from rest_framework import filters
# Create your views here.

class ListCreatePost(generics.ListCreateAPIView):
    serializer_class = PostDetailSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['Author','Title','Tags']
    def perform_create(self, serializer):
        serializer.save(Author = self.request.user)

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
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