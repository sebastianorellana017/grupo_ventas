from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ColourVariation, SizeVariation, Order, Product, OrderItem, Payment, Category, Address


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ColourVariationSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=False)
    class Meta:
        model = ColourVariation
        fields = ['name']
        read_only_fields = ['name']


class SizeVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariation
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    available_colours = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    available_sizes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'description', 'price', 'active', 'available_colours',
                  'available_sizes', 'category', 'stock']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'colour', 'size']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # billing_address =
    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    billing_address = serializers.SlugRelatedField(slug_field="address_line_1", queryset=Address.objects.all())
    shipping_address = serializers.SlugRelatedField(slug_field="address_line_2", queryset=Address.objects.all())
    
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    #user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


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
