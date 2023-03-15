from datetime import datetime

from django.db import models
from django.utils import timezone

from hotels.errors import InvalidTimeFormat
from pets.models import Pet


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    hourly_rate = models.FloatField(null=True)

    def board(self, pet, boarding_time=None):
        if boarding_time is None:
            boarding_time = timezone.now()
        else:
            try:
                # Convert 7:30PM to a "03/25/2020 07:30PM" datetime object
                date_format = "%m/%d/%Y"
                time_format = "%H:%M %p"
                current_date_string = timezone.now().strftime(date_format)
                boarding_time = datetime.strptime(
                    f"{current_date_string} {boarding_time}",
                    f"{date_format} {time_format}",
                )
            except ValueError:
                raise InvalidTimeFormat("Invalid time format. Must be something like '07:30 PM'.")

        self.boarding_records.create(pet=pet, boarding_time=boarding_time)

    def checkout(self, pet, checkout_time=None):
        if checkout_time is None:
            checkout_time = timezone.now()
        else:
            try:
                # Convert 7:30PM to a "03/25/2020 07:30PM" datetime object
                date_format = "%m/%d/%Y"
                time_format = "%H:%M %p"
                current_date_string = timezone.now().strftime(date_format)
                checkout_time = datetime.strptime(
                    f"{current_date_string} {checkout_time}",
                    f"{date_format} {time_format}",
                )
            except ValueError:
                raise InvalidTimeFormat("Invalid time format. Must be something like '07:30 PM'.")

        latest_boarding_record = self.boarding_records.last()
        latest_boarding_record.checkout_time = checkout_time
        latest_boarding_record.save()


class BoardingRecord(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="boarding_records", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name="boarding_records", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    boarding_time = models.DateTimeField()
    checkout_time = models.DateTimeField(null=True, blank=True)
