from rest_framework import serializers
from .models import Question,Answers,likes

class QuestionListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ['author','id','title','body','Code_picture']
        model = Question

class QuestionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
           'id',
           'author',
           'title',
           'Date_Added',
           'Date_updated',
        ]
        model = Answers

class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'parent',
            'Date_Added',
        ]
        model = Answers


class CommentDetailSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        fields = [
             'id',
             'author',
             'title',
             'answer',
             'Code_picture',
             'Date_Added',
             'Date_updated',
             'replies',
        ]
        model = Answers
    def get_replies(self,obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(),many = True).data
        return None