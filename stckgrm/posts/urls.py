from django.urls import path
from .views import ListCreatePost,UserPosts,PostDetails,Comm_ents

urlpatterns = [
    path('',ListCreatePost.as_view()),
    path('<uuid:pk>/',PostDetails.as_view()),
    path('<uuid:pk>/Comment',Comm_ents.as_view({'post':'create','get':'list'})),
    path('UserPosts/',UserPosts.as_view()),
]