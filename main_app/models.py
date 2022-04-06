from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Transaction(models.Model):
    transaction_number = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        # return self.transaction_number
         return str(self.transaction_number) + ": $" + str(self.balance)

STATUS_CHOICES = {
    ("Completed", "complete"), 
    ("Incomplete", "incomplete")
}

USER_CHOICES ={
    ("child", "child"),
    ("parent", "parent")
}

class Task(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duedate = models.DateTimeField()
    status = models.CharField(max_length=10, choices = STATUS_CHOICES)

    assigned_to = models.CharField(max_length=20, choices = USER_CHOICES)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction) # M:M example
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
        # return str(self.item) + ": $" + str(self.price)

    class Meta: 
        ordering = ['name']