from datetime import timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="ivan@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            creator=self.user,
            place="Место",
            time="11:00:00",
            action="Делать действие",
            habit_is_pleasant=False,
            connection_habit=None,
            number_of_executions=5,
            duration=timedelta(seconds=120),
            is_published=True,
            reward="Получение награды",
        )

    def test_habit_list(self):

        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_habit_is_published_list(self):

        url = reverse("habits:habit_is_published_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_habit_create(self):

        url = reverse("habits:habit_create")
        data = {
            "action": "Ничего не делать",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)

    def test_habit_update(self):

        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "reward": "Награда",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "Награда")

    def test_habit_delete(self):

        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)
