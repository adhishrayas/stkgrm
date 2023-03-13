from rest_framework import serializers
from .models import  User
from posts.models import Posts

class UserSerializer(serializers.ModelSerializer):

   class Meta:
       model = User
       fields = ['id','username','email','phone_no','Profile_picture','phone_no','first_name','last_name','Your_posts']