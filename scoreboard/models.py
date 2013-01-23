from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, unique=True)
    score = models.IntegerField(default=0)
