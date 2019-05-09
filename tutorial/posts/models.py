from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=60)
  body = models.TextField()
  user = models.ForeignKey(User, on_delete='CASCADE')
