from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kitchen.models import Dish


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    paginate_by = 5


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