from turtle import title
from django.db import models

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.title
