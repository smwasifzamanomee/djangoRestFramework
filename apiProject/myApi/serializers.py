from rest_framework import serializers

# created project folder then models then class name (Contact) imports
from myApi.models import Contact
from myApi.models import Product
from myApi.models import Order
from myApi.models import Snippet

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        # field = ['name', 'email', 'phone', 'desc', 'date']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # field = ['product_id', 'product_name', 'category', 'subcategory', 'price', 'desc', 'pub_date', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # field = ['order_id', 'items_json', 'name', 'email', 'address', 'city', 'state', 'zip_code', 'phone']

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
        # field = ['created', 'title', 'code', 'linenos', 'language', 'style']



