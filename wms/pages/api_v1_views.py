from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from stock.models import Product, Customer, Warehouse, Shipment
from stock.serializers import ProductSerializer, CustomerSerializer, WarehouseSerializer, ShipmentSerializer


#LIST API VIEWS
class Products(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):

    serializer_class = ProductSerializer


class Customers(generics.ListAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Warehouses(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class Shipments(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer            