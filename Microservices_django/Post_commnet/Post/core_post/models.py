from django.db import models

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    comments    = models.TextField(default="[]") # Empty arry/list
