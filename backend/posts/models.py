from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  year = models.IntegerField()
  medium = models.CharField(max_length=50)
  substrate = models.CharField(max_length=50)
  size = models.CharField(max_length=20)
  image = models.ImageField(upload_to="artwork/", blank=True)

  def __str__(self):
    return self.title
