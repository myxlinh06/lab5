from rest_framework.permissions import IsAuthenticated

class OrdersReportViewSet(viewsets.ModelViewSet):
    queryset = OrdersReport.objects.all()
    serializer_class = OrdersReportSerializer
    permission_classes = [IsAuthenticated]

class ProductReportViewSet(viewsets.ModelViewSet):
    queryset = ProductReport.objects.all()
    serializer_class = ProductReportSerializer
    permission_classes = [IsAuthenticated]
