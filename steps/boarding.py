from behave import given, when, then

from hotels.models import Hotel
from pets.models import Pet


@given('I empty the "Pets" table')
def step_impl(context):
    Pet.objects.all().delete()


@given("I create the following pets")
def step_impl(context):
    for row in context.table:
        Pet.objects.create(name=row["name"], breed=row["breed"])


@given('I empty the "Hotels" table')
def step_impl(context):
    Hotel.objects.all().delete()


@given("I create the following hotels")
def step_impl(context):
    for row in context.table:
        Hotel.objects.create(name=row["name"])


@when('I board "{pet_name}" to "{hotel_name}"')
def step_impl(context, pet_name, hotel_name):
    pet = Pet.objects.get(name=pet_name)
    hotel = Hotel.objects.get(name=hotel_name)
    hotel.board(pet)


@then('"{pet_name}" is boarded')
def step_impl(context, pet_name):
    pet = Pet.objects.get(name=pet_name)
    assert pet.is_boarded
