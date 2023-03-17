from rest_framework import serializers
from .models import Posts,Comments
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class PostDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    Author = serializers.ReadOnlyField(source = 'Author.Email')
    Upvote = serializers.BooleanField()
    Tags = TagListSerializerField()
    class Meta:
        fields = ['id','Author','Title','Date_Added','Tags','Body','Code_Field','Error_Field','Tags','Com_m_ents','Upvote']
        model = Posts

class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    Author = serializers.ReadOnlyField(source = 'Author.Email')
    Tags = TagListSerializerField()
    class Meta:
        fields = ['id','Author','Title','Date_Added','Tags','totalcomments','totalUpvotes',]
        model = Posts

class CommentsSerializer(serializers.ModelSerializer):
    Author = serializers.ReadOnlyField(source = 'Author.Email')
    post_id = serializers.ReadOnlyField()
    class Meta:
        fields = ['post_id','Author','Title','Body','Date_Added','Date_Edited','Correct_Code_Field']
        model = Comments
