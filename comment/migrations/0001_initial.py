# Generated by Django 4.1.7 on 2023-02-20 23:49

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comments",
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
                ("user_name", models.CharField(max_length=255)),
                ("mail", models.EmailField(max_length=255)),
                ("home_page", models.URLField(blank=True, max_length=255, null=True)),
                ("text", models.TextField()),
                ("modified", models.TimeField(auto_now_add=True)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="comment.comments",
                    ),
                ),
            ],
        ),
    ]
