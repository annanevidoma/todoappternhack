from django.db import models

class NewTask(models.Model):
    task = models.CharField(max_length=10000)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task
    #due_date = models.DateField(blank=True, null=True)
# Create your models here.
