from datetime import datetime

from django.db import models
from django.utils import timezone

from hotels.errors import InvalidTimeFormat
from hotels.utils import time_string_to_datetime
from pets.models import Pet


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    hourly_rate = models.FloatField(null=True)

    def board(self, pet, boarding_time=None):
        if boarding_time is None:
            boarding_time = timezone.now()
        else:
            boarding_time = time_string_to_datetime(boarding_time)

        self.boarding_records.create(pet=pet, boarding_time=boarding_time)

    def checkout(self, pet, checkout_time=None):
        if checkout_time is None:
            checkout_time = timezone.now()
        else:
            checkout_time = time_string_to_datetime(checkout_time)

        latest_boarding_record = self.boarding_records.filter(pet=pet).last()
        latest_boarding_record.checkout_time = checkout_time
        latest_boarding_record.save()


class BoardingRecord(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="boarding_records", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name="boarding_records", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    boarding_time = models.DateTimeField()
    checkout_time = models.DateTimeField(null=True, blank=True)
