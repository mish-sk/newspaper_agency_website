# Generated by Django 5.0.4 on 2024-04-19 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0002_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newspaper",
            options={"ordering": ["-published_date"]},
        ),
        migrations.AlterModelOptions(
            name="redactor",
            options={"ordering": ["last_name", "first_name", "username"]},
        ),
        migrations.AlterField(
            model_name="newspaper",
            name="publishers",
            field=models.ManyToManyField(
                related_name="newspaper", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
