from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from market.views import ProductsViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('products', ProductsViewSet, basename='Products')
router.register('categorys', CategoryViewSet, basename='Categorys')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
