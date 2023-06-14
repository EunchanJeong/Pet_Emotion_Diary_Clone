# Generated by Django 4.2 on 2023-06-13 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Personality",
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
                ("activity", models.CharField(max_length=1)),
                ("relationship", models.CharField(max_length=1)),
                ("proto_dog", models.CharField(max_length=1)),
                ("dependence", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("gender", models.CharField(max_length=1)),
                ("owner_name", models.CharField(max_length=15)),
                ("birth_day", models.DateField()),
                ("meet_day", models.DateField()),
                ("name", models.CharField(max_length=15)),
                ("kind", models.CharField(max_length=3)),
                (
                    "personality",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pet.personality",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_pet",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
