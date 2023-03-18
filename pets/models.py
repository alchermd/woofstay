from django.db import models


class Pet(models.Model):
    class Type(models.TextChoices):
        DOG = ("Dog", "Dog")
        CAT = ("Cat", "Cat")

    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    type = models.CharField(choices=Type.choices, max_length=255)

    @property
    def is_boarded(self):
        return self.boarding_records.filter(is_active=True)
