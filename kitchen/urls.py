from django.urls import path
from kitchen.views import CookListView, DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, \
    CookDetailView, CookUpdateView, CookDeleteView, DishTypeDetailView, DishTypeListView, DishTypeUpdateView, \
    DishTypeDeleteView, DishTypeCreateView

app_name = "kitchen"
urlpatterns = [
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
]