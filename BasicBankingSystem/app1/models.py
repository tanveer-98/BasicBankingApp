from django.db import models

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    current_balance = models.IntegerField()


    def __str__(self):
        return self.name
