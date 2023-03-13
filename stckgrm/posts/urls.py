from django.urls import path
from .views import ListCreatePost,UserPosts,PostDetails

urlpatterns = [
    path('',ListCreatePost.as_view()),
    path('<uuid:pk>/',PostDetails.as_view()),
    path('UserPosts/',UserPosts.as_view()),
]