from typing import Optional

from owners.models import Owner


def create_owner(
        *,
        first_name: str,
        last_name: Optional[str] = None,
        contact_number: str,
        address: Optional[str] = None,
) -> Owner:
    return Owner.objects.create(
        first_name=first_name,
        last_name=last_name,
        contact_number=contact_number,
        address=address,
    )
