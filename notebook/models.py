from django.db import models
from django.contrib.auth.models import User
import json


# Create your models here.
class Notes(models.Model):
    username = models.CharField(max_length=70)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=700)

    def __str__(self):
        return str(
            json.dumps({
                'username': self.username,
                'title': self.title,
                'desc': self.desc
            }))

    def __repr__(self):
        return str(
            json.dumps({
                'username': self.username,
                'title': self.title,
                'desc': self.desc
            }))
