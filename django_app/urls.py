from rest_framework.routers import DefaultRouter
from .views import ProductCategoryViewSet, ProductViewSet, CategoriesAndProductsView
from django.urls import path

router = DefaultRouter()
router.register(r'categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories_and_products/', CategoriesAndProductsView.as_view(), name='categories_and_products'),
]

urlpatterns += router.urls
