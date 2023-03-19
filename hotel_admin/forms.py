from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Submit
from django import forms

from pets.models import Pet

pet_details = Div(
    HTML("""
        <div class="card-header border-bottom">
            <h5 class="mb-0">Pet Details</h5>
        </div>
    """),

    Div(
        Div(
            Div(
                Field(
                    "pet_name",
                    placeholder="My name is..."
                ),
                css_class="col-12",
            ),
            Div(
                Field(
                    "pet_type",
                    css_class="form-select"
                ),
                css_class="col-md-6",
            ),
            Div(
                Field(
                    "pet_breed",
                    css_class="form-select"
                ),
                css_class="col-md-6",
            ),
            css_class="row g-3",
        ),
        css_class="card-body",
    ),
    css_class="card shadow",
)

owner_details = Div(
    HTML("""
        <div class="card-header border-bottom">
            <h5 class="mb-0">Owner Details</h5>
        </div>
    """),

    Div(
        Div(
            Div(
                Field(
                    "owner_first_name",
                    placeholder="Juan"
                ),
                css_class="col-6",
            ),
            Div(
                Field(
                    "owner_last_name",
                    placeholder="Dela Cruz"
                ),
                css_class="col-6",
            ),
            Div(
                Field(
                    "owner_contact_number",
                    placeholder="+639123456789"
                ),
                css_class="col-6",
            ),
            Div(
                Field(
                    "owner_address"
                ),
                css_class="col-md-12",
            ),
            css_class="row g-3",
        ),
        css_class="card-body",
    ),
    css_class="card shadow",
)

sample_breeds = {
    "Dog": (
        ("Siberian Husky", "Siberian Husky"),
        ("American Bully", "American Bully"),
        ("Norfolk Terrier", "Norfolk Terrier"),
    ),
    "Cat": (
        ("Siamese", "Siamese"),
        ("Persian", "Persian"),
    ),
}


class PetWithOwnerCreationForm(forms.Form):
    pet_name = forms.CharField(label="Pet Name", max_length=255)
    pet_type = forms.ChoiceField(label="Type", choices=Pet.Type.choices, initial=Pet.Type.DOG)
    pet_breed = forms.ChoiceField(label="Breed")
    owner_first_name = forms.CharField(label="First Name", max_length=255)
    owner_last_name = forms.CharField(label="Last Name", max_length=255, required=False)
    owner_contact_number = forms.CharField(label="Contact Number", max_length=255)
    owner_address = forms.CharField(label="Address", max_length=255, widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['pet_breed'].choices = sample_breeds[Pet.Type.DOG]
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        pet_details,
                        owner_details,
                        Div(
                            Submit("Save", "Save", css_class="btn btn-primary mb-0"),
                            css_class="text-end",
                        ),
                        css_class="vstack gap-4",
                    ),
                    css_class="col-lg-10 mx-auto",
                ),
                css_class="container",
            ),
        )
