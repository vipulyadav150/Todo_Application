from django.db import models
from datetime import *
# Create your models here.
app_name = 'todos'

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.title