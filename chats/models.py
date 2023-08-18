from django.conf import settings
from django.db import models
from django.utils import timezone
class chats(models.Model):
    author = models.CharField(max_length=250, null=True)
    sender = models.CharField(max_length=150, null=True)
    name = models.TextField(null=True)



    def __str__(self):
        return self.author

# Create your models here.
