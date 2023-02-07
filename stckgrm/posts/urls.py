from django.urls import path,include
from .views import QuestionDetailView,QuestionListView
# set urls for the posts app
urlpatterns = [
path('',QuestionListView.as_view()),
path('<uuid:pk>/',QuestionDetailView.as_view()),
]