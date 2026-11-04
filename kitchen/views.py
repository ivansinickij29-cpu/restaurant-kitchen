from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kitchen.forms import DishSearchForm
from kitchen.models import Dish, Cook


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
    fields = [
        "name",
        "description",
        "price",
        "dish_type",
        "cooks"
    ]
    success_url = reverse_lazy("kitchen:dish-list")

class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = [
        "name",
        "description",
        "price",
        "dish_type",
        "cooks"
    ]
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    paginate_by = 5


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