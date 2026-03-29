from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    CATEGORY = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('others', 'Others'),
    ]


    title = models.CharField(max_length=15)
    descriptions = models.TextField()
    due_date= models.DateField()
    due_time = models.TimeField()
    status = models.CharField(max_length=15, choices=STATUS, default= 'pending')
    category = models.CharField(max_length=15, choices=CATEGORY)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title