from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = models.ImageField(
        upload_to= "blog_image/",
        verbose_name="Фотография"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"