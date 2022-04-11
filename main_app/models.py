from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
    receiving_user = models.ForeignKey(User, related_name='receiving_user', on_delete=models.CASCADE)

    def __str__(self):
        # return self.transaction_number
         return ": $" + str(self.amount)

# class Transaction(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(default=timezone.now)
#     sending_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     receiving_user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         # return self.transaction_number
#          return ": $" + str(self.amount)

STATUS_CHOICES = {
    ("Not yet started", "not yet started"), 
    ("Completed", "complete"), 
    ("Incomplete", "incomplete")
}

# USER_CHOICES ={
#     ("child", "child"),
#     ("parent", "parent")
# }


class Task(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duedate = models.DateTimeField()
    description = models.CharField(max_length=200)
    task_status = models.CharField(max_length=20, choices = STATUS_CHOICES)
    task_approval = models.BooleanField()
    # user = models.ManyToManyField(User) # M:M example
    family = models.ManyToManyField(Family) # M:M example
    # transactions = models.ManyToManyField(Transaction) # M:M example
    # family = models.ForeignKey(Family, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
        # return str(self.item) + ": $" + str(self.price)

    class Meta: 
        ordering = ['name']


 
# class Transaction(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(default=timezone.now)
#     sending_user = models.ForeignKey(User, related_name='sending_user', on_delete=models.CASCADE)
#     receiving_user = models.ForeignKey(User, related_name='receiving_user', on_delete=models.CASCADE)

#     def __str__(self):
#         # return self.transaction_number
#          return ": $" + str(self.amount)