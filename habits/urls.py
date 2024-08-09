from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListApiView,
    HabitIsPublishedListApiView,
    HabitCreateApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListApiView.as_view(), name="habit_list"),
    path(
        "habit_is_published/",
        HabitIsPublishedListApiView.as_view(),
        name="habit_is_published_list",
    ),
    path("habits/create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("habits/update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_update"),
    path("habits/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habit_delete"),
]
