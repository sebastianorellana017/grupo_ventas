from rest_framework import serializers
from .models import ColourVariation, Order, Product, OrderItem, Payment

class ColourVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColourVariation
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = '__all__'
        fields = ['id','title', 'image', 'description', 'price', 'created', 'updated', 'active', 'available_colours',
                  'available_sizes','category', 'stock']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order','product','quantity', 'colour', 'size']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()

        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError(
                "Este nombre de usuario ya existe")
        else:
            return data