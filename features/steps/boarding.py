from behave import given, when, then

from hotels.errors import InvalidTimeFormat
from hotels.models import Hotel, BoardingRecord
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
        Hotel.objects.create(name=row["name"], hourly_rate=row.get("hourly_rate"))


@when('I board "{pet_name}" to "{hotel_name}" at "{boarding_time}"')
def step_impl(context, pet_name, hotel_name, boarding_time):
    try:
        pet = Pet.objects.get(name=pet_name)
        hotel = Hotel.objects.get(name=hotel_name)
        hotel.board(pet, boarding_time=boarding_time)
    except Exception as e:
        context.exception = e


@when('I board "{pet_name}" to "{hotel_name}"')
def step_impl(context, pet_name, hotel_name):
    pet = Pet.objects.get(name=pet_name)
    hotel = Hotel.objects.get(name=hotel_name)
    hotel.board(pet)


@when('"{pet_name}" checks out from "{hotel_name}" at "{checkout_time}"')
def step_impl(context, pet_name, hotel_name, checkout_time):
    try:
        pet = Pet.objects.get(name=pet_name)
        hotel = Hotel.objects.get(name=hotel_name)
        hotel.checkout(pet, checkout_time=checkout_time)
    except Exception as e:
        context.exception = e


@then('"{pet_name}" is boarded')
def step_impl(context, pet_name):
    pet = Pet.objects.get(name=pet_name)
    assert pet.is_boarded


@then('"{pet_name}"\'s boarding fee for his stay at "{hotel_name}" would be "{expected_boarding_fee:d}"')
def step_impl(context, pet_name, hotel_name, expected_boarding_fee):
    pet = Pet.objects.get(name=pet_name)
    hotel = Hotel.objects.get(name=hotel_name)
    computed_boarding_fee = pet.boarding_records.filter(hotel=hotel).last().total_fee
    assert computed_boarding_fee == expected_boarding_fee, f"{computed_boarding_fee} is not {expected_boarding_fee}"


@then("I get an error saying that the given time is invalid")
def step_impl(context):
    assert isinstance(context.exception, InvalidTimeFormat), "The time is deemed valid"


@given('I empty the "BoardingRecords" table')
def step_impl(context):
    BoardingRecord.objects.all().delete()


@then('"{record_count:d}" records are saved on "{pet_name}"\'s boarding history')
def step_impl(context, record_count, pet_name):
    pet = Pet.objects.get(name=pet_name)
    assert pet.boarding_records.count() == record_count
