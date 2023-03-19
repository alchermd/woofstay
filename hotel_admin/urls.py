from django.urls import path

from hotel_admin import views

urlpatterns = [
    path("pets/create/", views.CreatePetView.as_view(), name="create-pet"),
    path("breeds/", views.BreedListView.as_view(), name="breed-list"),
]

app_name = "hotel-admin"
