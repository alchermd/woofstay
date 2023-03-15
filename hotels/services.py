from hotels.models import Hotel
from pets.models import Pet


def compute_last_boarding_fee(*, pet: Pet, hotel: Hotel):
    last_boarding_record = hotel.boarding_records.filter(pet=pet).last()
    total_hours = (last_boarding_record.checkout_time - last_boarding_record.boarding_time).seconds / 3600
    return total_hours * hotel.hourly_rate
