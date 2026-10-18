from django.urls import path
from kitchen.views import DishListView


app_name = "kitchen"
urlpatterns = [
    path("dishes", DishListView.as_view(), name="dish-list"),
]