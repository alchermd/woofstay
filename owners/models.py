from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
