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
    