import uuid
from django.db import models
from posts.models import Question
from user.models import User
# Create your models here.

class Answers(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    post = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=400)
    answer_photo = models.ImageField(upload_to='/answers',blank=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    Date_Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Likes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    liked_object_post = models.ForeignKey(Question,blank=True,null=True,on_delete=models.CASCADE)
    liked_object_answer = models.ForeignKey(Answers,blank = True,null = True,on_delete=models.CASCADE)

    def __str__(self):
        return self.author


