from rest_framework import serializers
from .models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'parent', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'cost', 'description']
