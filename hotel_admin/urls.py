from django.urls import path

from hotel_admin import views

urlpatterns = [
    path("pets/create/", views.CreatePetView.as_view(), name="create-pet"),
    path("pets/<int:pk>/", views.PetDetailView.as_view(), name="pet-detail"),
    path("pets/", views.PetListView.as_view(), name="pet-list"),
    path("boarding-records/", views.BoardingRecordListView.as_view(), name="boarding-record-list"),
    path("breeds/", views.BreedListView.as_view(), name="breed-list"),
]

app_name = "hotel-admin"
