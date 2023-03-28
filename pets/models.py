from django.db import models

from owners.models import Owner


class Pet(models.Model):
    class Type(models.TextChoices):
        DOG = ("Dog", "Dog")
        CAT = ("Cat", "Cat")

    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    type = models.CharField(choices=Type.choices, max_length=255)
    owners = models.ManyToManyField(Owner, related_name="pets")

    @property
    def is_boarded(self):
        return self.boarding_records.filter(is_active=True)

    def add_owner(self, owner: Owner):
        self.owners.add(owner)

    @property
    def primary_owner(self):
        # TODO: Make this more dynamic and not just index based
        return self.owners.first()

    def __str__(self):
        return f"{self.name} the {self.breed}"
