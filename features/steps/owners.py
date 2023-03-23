from behave import given, when, then, step

from features.utils import null_to_none
from owners.models import Owner
from owners.services import create_owner
from pets.models import Pet


@given('I empty the "Owners" table')
def step_impl(context):
    Owner.objects.all().delete()


@step('I add "{first_name}" "{last_name}", with contact "{contact_number}", and address "{address}" into the system')
def step_impl(context, first_name, last_name, contact_number, address):
    create_owner(first_name=first_name, last_name=last_name, contact_number=contact_number, address=address)


@step('I add "{first_name}", with contact "{contact_number}" into the system')
def step_impl(context, first_name, contact_number):
    create_owner(first_name=first_name, contact_number=contact_number)


@then('the following records are saved in the "Owners" table')
def step_impl(context):
    for row in context.table:
        Owner.objects.get(
            first_name=row["first_name"],
            last_name=null_to_none(row["last_name"]),
            contact_number=row["contact_number"],
            address=null_to_none(row["address"]),
        )


@when('I set "{first_name}" "{last_name}" as "{pet_name}"\'s owner')
def step_impl(context, first_name, last_name, pet_name):
    pet = Pet.objects.get(name=pet_name)
    owner = Owner.objects.get(first_name=first_name, last_name=last_name)
    pet.add_owner(owner)


@then('I get "{first_name}" "{last_name}"\'s record when I fetch "{pet_name}"\'s owner records')
def step_impl(context, first_name, last_name, pet_name):
    pet = Pet.objects.get(name=pet_name)
    owner = Owner.objects.get(first_name=first_name, last_name=last_name)
    assert owner in pet.owners.all()


@then('I get "{first_name}" "{last_name}"\'s record when I fetching "{pet_name}"\'s primary owner')
def step_impl(context, first_name, last_name, pet_name):
    pet = Pet.objects.get(name=pet_name)
    owner = Owner.objects.get(first_name=first_name, last_name=last_name)
    assert pet.primary_owner == owner
