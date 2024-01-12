from django.db import models
from user_management.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
