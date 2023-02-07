from rest_framework import serializers
from .models import Question

class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id','title','body','Code_picture']
        model = Question

class QuestionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question