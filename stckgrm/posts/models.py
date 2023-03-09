import uuid
from django.db import models
from user.models import User
# Create your models here.

class Question(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150,unique=True)
    body = models.TextField(max_length=250)
    Code_picture = models.ImageField(upload_to='questions/',blank=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    def comments_total(self):
        return Answers.objects.filter(post_id = self.id).count()
    
    def comments(self):
        array = []
        for comment in Answers.objects.filter(post_id = self.id):
            c = {}
            c['body'] = comment.answer
            c['created_at'] = comment.Date_Added
            c['creator'] = comment.author
            c['code_pic'] = comment.Code_picture

            array.append(c)
        return array
    


class Answers(models.Model):
    post = models.OneToOneField(Question,on_delete=models.CASCADE,primary_key=True)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.TextField(max_length=50)
    answer = models.TextField(max_length=200)
    Code_picture = models.ImageField(upload_to='questions/answers',blank=True)
    parent = models.ForeignKey('self',null = True,blank = True,on_delete= models.CASCADE)
    is_parent = models.BooleanField(default=True)
    Date_Added = models.DateTimeField(auto_now_add=True)
    Date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.author) + 'comment' + str(self.answer)
    
    def children(self):
        return Answers.objects.filter(parent = self)
    
    
class likes(models.Model):
    post = models.ForeignKey(Question,on_delete = models.CASCADE)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    Date_Added = models.DateTimeField(auto_now_add = True)
    Date_updated = models.DateTimeField(auto_now = True)