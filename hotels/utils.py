from datetime import datetime

from django.utils import timezone

from hotels.errors import InvalidTimeFormat


def time_string_to_datetime(time_string):
    try:
        # Convert 7:30PM to a "03/25/2020 07:30PM" datetime object
        date_format = "%m/%d/%Y"
        time_format = "%H:%M %p"
        current_date_string = timezone.now().strftime(date_format)
        return datetime.strptime(
            f"{current_date_string} {time_string}",
            f"{date_format} {time_format}",
        )
    except ValueError:
        raise InvalidTimeFormat("Invalid time format. Must be something like '07:30 PM'.")
