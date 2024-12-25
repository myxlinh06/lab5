from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrdersReportViewSet, ProductReportViewSet

router = DefaultRouter()
router.register(r'reports/orders', OrdersReportViewSet)
router.register(r'reports/products', ProductReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
