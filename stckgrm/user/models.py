from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,blank=True,null=True,unique=True)
    email = models.EmailField(_('email address'),unique=True)
    native_name = models.TextField(max_length=100)
    phone_no = PhoneNumberField()
    Profile_picture = models.ImageField(upload_to='profile/',blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','Profile_picture','phone_no']

    def __str__(self):
        return "{}".format(self.email)