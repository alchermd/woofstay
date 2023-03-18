from pets.models import Pet


def create_pet(*, name, breed, type):
    Pet.objects.create(name=name, breed=breed, type=type)
