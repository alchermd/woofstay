from django.contrib import messages
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from hotel_admin.forms import PetWithOwnerCreationForm, sample_breeds
from owners.services import create_owner
from pets.models import Pet
from pets.services import create_pet


class CreatePetView(FormView):
    template_name = "hotel_admin/pets/create.html"
    form_class = PetWithOwnerCreationForm
    success_url = reverse_lazy("hotel-admin:pet-list")

    def form_valid(self, form):
        pet = create_pet(
            name=form.cleaned_data["pet_name"],
            type=form.cleaned_data["pet_type"],
            breed=form.cleaned_data["pet_breed"],
        )
        owner = create_owner(
            first_name=form.cleaned_data["owner_first_name"],
            last_name=form.cleaned_data["owner_last_name"],
            contact_number=form.cleaned_data["owner_contact_number"],
            address=form.cleaned_data["owner_address"],
        )
        pet.add_owner(owner)

        messages.success(self.request, "Pet record has been created!")
        return super().form_valid(form)


class BreedListView(View):
    def get(self, request):
        # TODO: Replace this with a DRF view?
        if pet_type := request.GET.get("pet_type"):
            if not (breeds := sample_breeds.get(pet_type)):
                return HttpResponseNotFound()
            return JsonResponse(breeds, safe=False)
        return HttpResponseBadRequest()


class PetListView(View):
    def get(self, request):
        pets = Pet.objects.all().order_by("-id")
        return render(request, "hotel_admin/pets/list.html", {"pets": pets})
