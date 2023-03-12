from django.db import models

from pets.models import Pet


class Hotel(models.Model):
    name = models.CharField(max_length=255)

    def board(self, pet):
        self.boarding_records.create(pet=pet)


class BoardingRecord(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="boarding_records", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name="boarding_records", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
