from django.db import models
from post.models.response import Response

class Post(models.Model):
    postText = models.CharField(max_length=255)
    username = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    response = models.ForeignKey(Response)

    def __str__(self):
        return self.name