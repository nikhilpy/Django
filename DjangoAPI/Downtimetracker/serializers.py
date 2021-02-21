from rest_framework import serializers
from Downtimetracker.models import Customer, Product, ProdURL, Outages

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		field = ('CustomerID', 'CustomerName')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		field = ('ProductID', 'ProductName')

class ProdURLSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProdURL
		field = ('PLinkID', 'ProdLink')

class OutagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Outages
		field = ('OutageID', 'ActivityType', 'OutageStartTime', 'OutageEndTime', 'OutageDuration', 'Outageremarks')