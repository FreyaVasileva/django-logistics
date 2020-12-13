from django.contrib.auth.models import User
from django.db import models


class Consignment(models.Model):
    STATUS_CHOICES = (
        ('pending_delivery', 'PENDING_DELIVERY'),
        ('delivered', 'DELIVERED'),
        ('cancelled', 'CANCELLED'),
    )
    tracking_number = models.IntegerField(blank=False, unique=True, error_messages={'unique': "already been register"})
    delivery_date = models.DateField(blank=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending_delivery')
    receiver = models.ForeignKey(User, limit_choices_to={'groups': 1}, on_delete=models.CASCADE)
