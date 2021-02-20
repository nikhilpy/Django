from django.db import models

# Create your models here.

class Customer(models.Model):
	CustomerID = models.AutoField(primary_key=True)
	CustomerName = models.CharField(max_length=50)

class Product(models.Model):
	ProductID = models.AutoField(primary_key=True)
	ProductName = models.CharField(max_length=50)

class ProdURL(models.Model):
	PLinkID = models.AutoField(primary_key=True)
	ProdLink = models.CharField(max_length=100)

class Outages(models.Model):
	OutageID = models.AutoField(primary_key=True)
	ActivityType = models.BooleanField(False)
	OutageStartTime = models.DateTimeField()
	OutageEndTime = models.DateTimeField()
	OutageDuration = models.DurationField()
	Outageremarks = models.CharField(max_length=500)