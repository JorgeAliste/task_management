from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    time_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.task}-{self.completed}"
