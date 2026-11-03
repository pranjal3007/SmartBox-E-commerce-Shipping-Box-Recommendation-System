
from rest_framework import serializers
from django.db import transaction

from .models import Product, Box, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'length',
            'width',
            'height',
            'weight',
        ]
        read_only_fields = ['id']


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = [
            'id',
            'name',
            'internal_length',
            'internal_width',
            'internal_height',
            'max_weight',
            'cost',
        ]
        read_only_fields = ['id']


class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'quantity',
        ]
        read_only_fields = ['id', 'product_name']


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'created_at',
            'items',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_items(self, value):

        if not value:
            raise serializers.ValidationError(
                "An order must contain at least one product."
            )

        product_ids = [
            item['product'].id for item in value
        ]

        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError(
                "Duplicate products are not allowed. "
                "Increase the quantity instead."
            )

        return value

    @transaction.atomic
    def create(self, validated_data):

        items_data = validated_data.pop('items')

        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(
                order=order,
                **item
            )

        return order

    @transaction.atomic
    def update(self, instance, validated_data):

        items_data = validated_data.pop('items', None)

        instance.order_number = validated_data.get(
            'order_number',
            instance.order_number
        )

        instance.save()

        if items_data is not None:

            instance.items.all().delete()

            for item in items_data:
                OrderItem.objects.create(
                    order=instance,
                    **item
                )

        return instance
