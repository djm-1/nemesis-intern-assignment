from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=300,blank=False)
    def __str__(self):
        return self.user.username 