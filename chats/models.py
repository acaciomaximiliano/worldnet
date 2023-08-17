from django.db import models

class Chats(models.Model):
    author = models.CharField(max_length=250, null=True)
    sender = models.CharField(max_length=200, null=True)
    name = models.TextField()



    def __str__(self):
        return self.author

# Create your models here.
