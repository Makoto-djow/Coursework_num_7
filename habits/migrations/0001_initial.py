# Generated by Django 4.2.2 on 2024-08-08 13:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Место выполнения",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Время выполнения"
                    ),
                ),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "habit_is_pleasant",
                    models.BooleanField(
                        default=True, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "number_of_executions",
                    models.IntegerField(
                        default=1, verbose_name="Количество выполнений в неделю"
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Продолжительность выполнения",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "connection_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habits",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
