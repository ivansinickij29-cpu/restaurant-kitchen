from django.urls import path
from kitchen.views import DishListView, DishDetailView

app_name = "kitchen"
urlpatterns = [
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
]