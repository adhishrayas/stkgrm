from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class UserEditview(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request,pk):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
        
