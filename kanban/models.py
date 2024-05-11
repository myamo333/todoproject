# kanban/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ])

    def __str__(self):
        return self.title
