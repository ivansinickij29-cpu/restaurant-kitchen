from django.urls import reverse
from django.test import TestCase

from kitchen.models import DishType, Cook, Dish


class DishTypeTests(TestCase):
    def test_create_dish_type(self):
        dish_type = DishType.objects.create(name="Pizza")

        self.assertEqual(dish_type.name, "Pizza")

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Soup")
        self.assertEqual(str(dish_type), "Soup")

    def test_dish_type_counts(self):
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Soup")
        count = DishType.objects.count()
        self.assertEqual(count, 2)


class DishListViewTests(TestCase):
    def setUp(self):
        user = Cook.objects.create_user(username="test", password="test123")
        self.client.force_login(user)

    def test_search_dishes(self):
        dish_type = DishType.objects.create(name="Pizza")
        Dish.objects.create(name="Margherita Pizza", price=25.00, dish_type=dish_type)
        Dish.objects.create(name="Papperoni Pizza", price=20.00, dish_type=dish_type)
        response = self.client.get(
            "/dishes/",
            {
                "name": "Margherita",
            },
        )
        self.assertContains(response, "Margherita Pizza")
        self.assertNotContains(response, "Papperoni Pizza")


class DishModelTests(TestCase):
    def test_dish_type_relation(self):
        dish_type = DishType.objects.create(name="Pizza")
        dish = Dish.objects.create(
            name="Margherita Pizza", price=25.00, dish_type=dish_type
        )
        self.assertEqual(dish.dish_type, dish_type)


class CookDeleteViewTests(TestCase):
    def test_regular_user_cannot_delete_cook(self):
        user = Cook.objects.create_user(username="test", password="test1234")
        cook = Cook.objects.create_user(username="test_cooks", password="test_cook123")
        self.client.force_login(user)
        response = self.client.post(reverse("kitchen:cook-delete", args=[cook.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Cook.objects.filter(pk=cook.pk).exists())

    def test_superuser_can_delete_cook(self):
        admin = Cook.objects.create_superuser(username="admin", password="admin123")
        cook = Cook.objects.create_user(username="test_cooks", password="test_cook123")
        self.client.force_login(admin)
        response = self.client.post(reverse("kitchen:cook-delete", args=[cook.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Cook.objects.filter(pk=cook.pk).exists())
