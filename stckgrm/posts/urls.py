from django.urls import path,include
from .views import QuestionDetailView,QuestionListView,CommentDetailsView,CommentCreateView
# set urls for the posts app
urlpatterns = [
path('',QuestionListView.as_view()),
path('<uuid:pk>/',QuestionDetailView.as_view()),
path('<uuid:pk>/comments',CommentCreateView.as_view()),
path('<uuid:pk>/comments/edit',CommentDetailsView.as_view()),
]