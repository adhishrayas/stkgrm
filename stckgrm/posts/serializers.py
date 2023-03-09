from rest_framework import serializers
from .models import Question,Answers,likes

class QuestionListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ['author','id','title','body','Code_picture','comments_total']
        model = Question

class QuestionDetailsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        fields = ['author','id','title','body','Code_picture','comments_total']
        model = Question

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source ='author.username')
    post = serializers.ReadOnlyField('post')
    class Meta:
        fields = [
           'post',
           'author',
           'title',
           'Date_Added',
           'Date_updated',
        ]
        model = Answers

class CommentChildSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = [
            'id',
            'parent',
            'author',
            'Date_Added',
        ]
        model = Answers


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        fields = [
             'post',
             'author',
             'title',
             'answer',
             'Code_picture',
             'Date_Added',
             'Date_updated',
        ]
        model = Answers
