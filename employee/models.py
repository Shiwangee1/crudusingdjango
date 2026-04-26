from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()

    phone = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name