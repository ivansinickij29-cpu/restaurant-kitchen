from django.urls import path
from kitchen.views import DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView

app_name = "kitchen"
urlpatterns = [
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete")
]