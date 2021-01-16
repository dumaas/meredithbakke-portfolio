import uuid
from django.db import models
from django.urls import reverse


class Post(models.Model):
  id = models.UUIDField(
      primary_key=True,
      default=uuid.uuid4,
      editable=False)
  author = models.CharField(max_length=200, default="Meredith Bakke")
  title = models.CharField(max_length=50)
  year = models.IntegerField()
  medium = models.CharField(max_length=50)
  substrate = models.CharField(max_length=50)
  size = models.CharField(max_length=20)
  image = models.ImageField(upload_to="artwork/", blank=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])
