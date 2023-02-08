from django.urls import path
from .views import UserView,UserEditview

urlpatterns = [
    path('',UserView.as_view()),
    path('<uuid:pk>',UserEditview.as_view()),
]
