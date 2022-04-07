from django.contrib import admin
from .models import Task, Transaction, Family, Assignment


# Register your models here.

admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(Family)
admin.site.register(Assignment)
