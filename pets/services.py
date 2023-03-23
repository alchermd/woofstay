from pets.models import Pet


def create_pet(*, name: str, breed: str, type: str) -> Pet:
    return Pet.objects.create(name=name, breed=breed, type=type)
