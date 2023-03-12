from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)

    @property
    def is_boarded(self):
        return self.boarding_records.filter(is_active=True)
