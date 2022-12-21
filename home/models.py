from django.db import models

# Create your models here.
class Task(models.Model):
    status_choice = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Complete','Complete')
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50,choices=status_choice)

    def __str__(self):
        return self.name
