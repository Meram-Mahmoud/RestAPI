
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)  # True for completed, False for pending

    def __str__(self):
        return self.title
