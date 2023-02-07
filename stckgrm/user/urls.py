from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('',UserDetailView.as_view()),
]
