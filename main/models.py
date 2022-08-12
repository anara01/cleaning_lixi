from django.db import models
from django.urls import reverse
# Create your models here.

class Team(models.Model):
    """Команда"""
    image = models.ImageField("Фото")
    name = models.CharField("Имя", max_length=50)
    lastname = models.CharField("Фамилия", max_length=50)
    jobteam = models.CharField("Профессия", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"