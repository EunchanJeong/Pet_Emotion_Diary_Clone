from django.urls import path

from .views import base_views, pet_views

app_name = "pet"

urlpatterns = [
    path("", base_views.index, name="index"),
    path("<int:pet_id>/", base_views.detail, name="detail"),
    path("create/", pet_views.pet_create, name="pet_create"),
    path(
        "modify/<int:pet_id>/<str:request_url>/",
        pet_views.pet_modify,
        name="pet_modify",
    ),
    path("delete/<int:pet_id>/", pet_views.pet_delete, name="pet_delete"),
]
