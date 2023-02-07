from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from stckgrm.permissions.permissions import IsAuthorOrReadOnly
# Create your views here.


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
