from pets.models import Pet


def create_pet(*, name, breed):
    Pet.objects.create(name=name, breed=breed)
