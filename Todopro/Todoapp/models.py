from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    isCompleted = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

     