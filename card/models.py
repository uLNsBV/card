from pydoc import describe
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=25, null=True)
    title = models.CharField(max_length=250)
    describtion = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images')

    def __str__(self) -> str:
        return f'{self.title} -> {self.author}'
