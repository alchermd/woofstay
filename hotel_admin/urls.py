from django.urls import path

from hotel_admin import views

urlpatterns = [
    path("pets/create/", views.CreatePetView.as_view(), name="create-pet"),
]

app_name = "hotel-admin"
