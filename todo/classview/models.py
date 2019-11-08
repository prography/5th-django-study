from django.db import models

class Todo(models.Model):
    complete = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True)
