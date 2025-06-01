from django.db import models
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    reservation_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')])
