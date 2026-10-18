from django.contrib import admin

from kitchen.models import DishType, Dish, Cook

admin.site.register(DishType)
admin.site.register(Cook)
admin.site.register(Dish)
