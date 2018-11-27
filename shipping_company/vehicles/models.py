from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    kilometers = models.IntegerField()

    def __str__(self):
        return self.brand + " " + self.model


class Driver(models.Model):
    vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
