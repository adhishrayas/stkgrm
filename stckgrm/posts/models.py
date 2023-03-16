import uuid
from django.db import models
from user.models import User
from taggit.managers import TaggableManager


# Create your models here.


class PostsManager(models.Manager):
    
    def create_post(self,Title:str,Body:str,Code_Field:str,Error_Field:str,Tags:str)-> 'Posts':
        if not Title:
            raise ValueError('Post must have a Title')
        if not Tags:
            raise ValueError('Post must have Tags')
        if not Body:
            raise ValueError('Post must have a Body')
        if not Error_Field:
            raise Warning('Error Field will ensure a better understanding of your problem!')
        if not Code_Field:
            raise Warning('Code Field will ensure a better understanding of your problem!')
        
        post = self.model()
        post.Title = Title
        post.Body = Body
        post.Error_Field = Error_Field
        post.Code_Field = Code_Field
        post.Tags = Tags
        post.save()
        return post


class CommentsManager(models.Manager):
   def create_comments(self,Title,Body,**args)-> 'Comments':
       if not Title:
           raise ValueError('Title is necessary')
       if not Body:
           raise ValueError('Body is necessary')
       comment = self.model(Title,Body,**args)
       comment.save()
       return comment
    

class Posts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=255,blank=False,unique=True)
    Body = models.TextField(max_length=300,blank=False)
    Code_Field = models.TextField(blank=True)
    Error_Field = models.TextField(blank=True)
    Date_Added = models.DateTimeField(auto_now_add=True)
    Date_Edited = models.DateTimeField(auto_now=True)
    Tags = TaggableManager()
    objects = PostsManager()

    def __str__(self):
        return self.Title
    
    @property
    def Com_m_ents(self):
        array = []
        for comment in Comments.objects.filter(post_id = self.id):
            c = {}
            c['Body'] = comment.Body
            c['Title'] = comment.Title
            c['Author']= comment.Author.username
            c['Date_Added']= comment.Date_Added
            array.append(c)
        return array

class Comments(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
        )          
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=255,blank=False,null=True)
    Body = models.TextField(max_length=255,blank=False,null=False)
    Date_Added = models.DateTimeField(auto_now_add=True)
    Date_Edited = models.DateTimeField(auto_now=True)
    Correct_Code_Field = models.TextField(blank=True)
    objects = CommentsManager()

    def __str__(self):
        return self.Title
    


