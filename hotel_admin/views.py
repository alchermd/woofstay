from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from hotel_admin.forms import PetWithOwnerCreationForm, sample_breeds


class CreatePetView(View):
    def get(self, request):
        form = PetWithOwnerCreationForm()
        return render(request, "hotel_admin/pets/create.html", {"form": form})


class BreedListView(View):
    def get(self, request):
        # TODO: Replace this with a DRF view?
        if pet_type := request.GET.get("pet_type"):
            if not (breeds := sample_breeds.get(pet_type)):
                return HttpResponseNotFound()
            return JsonResponse(breeds, safe=False)
        return HttpResponseBadRequest()
