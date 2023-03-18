from behave import given, when, then

from features.utils import null_to_none
from owners.models import Owner
from owners.services import create_owner


@given('I empty the "Owners" table')
def step_impl(context):
    Owner.objects.all().delete()


@when('I add "{first_name}" "{last_name}", with contact "{contact_number}", and address "{address}" into the system')
def step_impl(context, first_name, last_name, contact_number, address):
    create_owner(first_name=first_name, last_name=last_name, contact_number=contact_number, address=address)


@when('I add "{first_name}", with contact "{contact_number}" into the system')
def step_impl(context, first_name, contact_number):
    create_owner(first_name=first_name, contact_number=contact_number)


@then('the following records are saved in the "Owners" table')
def step_impl(context):
    for row in context.table:
        print(null_to_none(row["last_name"]))
        Owner.objects.get(
            first_name=row["first_name"],
            last_name=null_to_none(row["last_name"]),
            contact_number=row["contact_number"],
            address=null_to_none(row["address"]),
        )
