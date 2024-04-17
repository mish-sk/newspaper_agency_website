from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from newspaper_agency_website import settings


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = [
            "username",
            "last_name",
            "first_name"
        ]

    def __str__(self):
        return(
            f"{self.first_name} {self.last_name} ({self.username})"
        )

    def get_absolute_url(self):
        return reverse("newspaper:redactor_detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["-published_date", ]

    def __str__(self):
        return f"{self.title} ({self.published_date})"
