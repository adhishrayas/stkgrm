from rest_framework import serializers
from .models import Question

class QuestionListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ['author','id','title','body','Code_picture']
        model = Question

class QuestionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question