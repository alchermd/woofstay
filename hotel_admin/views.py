from django.shortcuts import render
from django.views import View


class CreatePetView(View):
    def get(self, request):
        return render(request, "hotel_admin/pets/create.html")
