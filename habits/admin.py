from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "creator",
        "is_published",
    )
    list_filter = ("creator",)
    search_fields = ("action",)