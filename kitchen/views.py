from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from kitchen.forms import DishSearchForm, CookSearchForm, DishTypeSearchForm
from kitchen.models import Dish, Cook, DishType


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset


class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username:
                queryset = queryset.filter(username__icontains=username)
        return queryset


class CookDetailView(LoginRequiredMixin, DetailView):
    model = Cook


class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    fields = [
        "first_name",
        "last_name",
        "years_of_experience",
    ]
    success_url = reverse_lazy("kitchen:cook-list")

    def get_object(self, queryset=None):
        cook = super().get_object(queryset)
        if cook != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return cook


class CookDeleteView(LoginRequiredMixin, DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")

    def get_object(self, queryset=None):
        cook = super().get_object(queryset)
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return cook


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset


class DishTypeDetailView(LoginRequiredMixin, DetailView):
    model = DishType


class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
