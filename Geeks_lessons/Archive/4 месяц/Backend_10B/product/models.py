from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo_image/",
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Тел номер"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    whatsapp_url = models.URLField(
        verbose_name="Whatsapp url"
    )
    instagram_url = models.URLField(
        verbose_name="instagram url"
    )
    youtube_url = models.URLField(
        verbose_name="youtube url"
    )
    class Meta:
        verbose_name = "Основные Настройки"
        verbose_name_plural = "Основная Настройка"