from behave import when, then

from pets.models import Pet
from pets.services import create_pet


@when('I add "{pet_name}" the "{pet_breed}" into the system')
def step_impl(context, pet_name, pet_breed):
    create_pet(name=pet_name, breed=pet_breed)


@then('the following records are saved in the "Pets" table')
def step_impl(context):
    for row in context.table:
        Pet.objects.get(name=row["name"], breed=row["breed"])
