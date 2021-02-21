from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Downtimetracker.models import Customer,Product,ProdURL,Outages
from Downtimetracker.serializers import CustomerSerializer,ProductSerializer,ProdURLSerializer,OutagesSerializer
# Create your views here.

@csrf_exempt
def CustomerAPI(request,id=0):

	if request.method=='GET':
		customers = Customers.objects.all()
		customers_serializer = CustomerSerializer(Customer, many=True)
		return JsonResponse(customers_serializer.data, safe=False)

	elif request.method=='POST':
		customer_data=JSONParser().parse(request)
		customer_serializer = CustomerSerializer(data=customer_data)
		if customer_serializer.is_valid():
			customer_serializer.save()
			return JsonResponse("Added Successfully!!", safe=False)
		return JsonResponse("Failed to Add.", safe=False)

	elif request.method=='PUT':
		customer_data = JSONParser().parse(request)
		customer=Customers.objects.get(CustomerID=customer_data['CustomerID'])
		customer_serializer=CustomerSerializer(customer,data=customer_data)
		if customer_serializer.is_valid():
			customer_serializer.save()
			return JsonResponse("Update Successfully!!", safe=False)
		return JSONParser("Failed to update", safe=False)

	elif request.method=="DELETE":
		customer=Customers.objects.get(CustomerID=id)
		department.delete()
		return JsonResponse("Deleted Successfully!!", safe=False)