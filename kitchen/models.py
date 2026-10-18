from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.PROTECT, related_name="dishes")
    cooks = models.ManyToManyField("Cook", related_name="dishes")

    def __str__(self):
        return f"{self.name} — {self.price}"


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.years_of_experience or 0} years)"
