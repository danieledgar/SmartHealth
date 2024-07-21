from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):
    temperature=models.IntegerField()
    steps_walked=models.IntegerField()
    heart_beat=models.IntegerField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author