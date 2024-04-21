from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    rewardPoints = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.firstName+self.lastName