from django.urls import path,include
from .views import QuestionDetailView,QuestionListView,CommentDetailsView,CommentListView
# set urls for the posts app
urlpatterns = [
path('',QuestionListView.as_view()),
path('<uuid:pk>/',QuestionDetailView.as_view()),
path('<uuid:pk>/comments',CommentListView.as_view()),
path('<uuid:pk>/comments/edit',CommentDetailsView.as_view()),
]