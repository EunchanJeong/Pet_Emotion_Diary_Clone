# Generated by Django 4.2 on 2023-06-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0003_alter_diary_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diary",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="diary_images/"),
        ),
    ]
