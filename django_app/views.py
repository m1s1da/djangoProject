from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesAndProductsView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        products = Product.objects.all()

        categories_data = [{
            "id": category.id,
            "name": category.name,
            "parent_id": category.parent.id if category.parent else None,
            "subcategories": list(category.subcategories.values_list('id', flat=True)),
            "product_ids": list(category.products.values_list('id', flat=True))
        }
            for category in categories
        ]

        products_data = [
            {
                "id": product.id,
                "name": product.name,
                "category_id": product.category.id,
                "cost": product.cost,
                "description": product.description
            }
            for product in products
        ]

        response_data = {
            "categories": categories_data,
            "products": products_data
        }

        return Response(response_data)
