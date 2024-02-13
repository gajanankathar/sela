from django.db import models


class Task(models.Model):
    COMPLETION_STATUS = [
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=COMPLETION_STATUS)

    def __str__(self):
        return self.title
