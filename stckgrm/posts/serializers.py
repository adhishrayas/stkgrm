from rest_framework import serializers
from .models import Posts
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class PostDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    Author = serializers.ReadOnlyField(source = 'Author.Email')
    Tags = TagListSerializerField()
    class Meta:
        fields = ['id','Author','Title','Date_Added','Tags','Body','Code_Field','Error_Field','Tags']
        model = Posts

class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    Author = serializers.ReadOnlyField(source = 'Author.Email')
    Tags = TagListSerializerField()
    class Meta:
        fields = ['id','Author','Title','Date_Added','Tags']
        model = Posts
