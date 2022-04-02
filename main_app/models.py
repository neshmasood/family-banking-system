from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS_CHOICES = {
    ("Yes", "complete"), 
    ("No", "incomplete")
}

class Task(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duedate = models.DateTimeField()
    status = models.CharField(max_length=10, choices = STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
        # return str(self.item) + ": $" + str(self.price)

    class Meta: 
        ordering = ['name']