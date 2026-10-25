from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Cook

admin.site.register(DishType)


class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ("kitchen info", {"fields" : ("years_of_experience",)}),
    )
admin.site.register(Cook, CookAdmin)
admin.site.register(Dish)
