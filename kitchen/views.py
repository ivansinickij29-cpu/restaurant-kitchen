from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from kitchen.models import Dish


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish
