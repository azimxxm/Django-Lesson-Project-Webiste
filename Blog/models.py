from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nomlanishi")
    discrition = models.TextField(max_length=5000, verbose_name="Ma'lumot")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Mualif")
    is_published = models.BooleanField(default=False, verbose_name="Tekshirilgan")
    image = models.ImageField(upload_to="Post/", verbose_name="Rasm")
    date_created = models.DateField(auto_now_add=True, verbose_name="Kiritish vaqti")
    date_updated = models.DateField(auto_now=True, verbose_name="Yangilanish vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Post"
        verbose_name = "Post"


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nomlanishi")
    date_created = models.DateField(auto_now_add=True, verbose_name="Kiritish vaqti")
    date_updated = models.DateField(auto_now=True, verbose_name="Yangilanish vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Service"
        verbose_name = "Service"


class Pricing(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tarif")
    price = models.PositiveIntegerField(verbose_name="Narx")
    is_active = models.BooleanField(default=False, verbose_name="Faol")
    service = models.ManyToManyField(Service,  verbose_name="Xizmat")
    date_created = models.DateField(auto_now_add=True, verbose_name="Kiritish vaqti")
    date_updated = models.DateField(auto_now=True, verbose_name="Yangilanish vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Pricing"
        verbose_name = "Pricing"
