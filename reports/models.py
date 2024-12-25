from django.db import models

class OrdersReport(models.Model):
    order_id = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Report {self.id} - Order ID {self.order_id}"

class ProductReport(models.Model):
    order_report = models.ForeignKey(OrdersReport, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    total_sold = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product Report {self.id} - Product ID {self.product_id}"
