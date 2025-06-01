from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)  # e.g., 'kg', 'liters'
    last_updated = models.DateTimeField(auto_now=True)
