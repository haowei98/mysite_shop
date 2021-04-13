from django.db import models
import uuid


class Buyer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial = models.CharField(max_length=50, blank=True, null=True)
    imei = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    order_id = models.CharField(max_length=15)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    last_active = models.DateTimeField(auto_now=True)
