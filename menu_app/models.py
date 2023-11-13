from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL, PROTECT, CASCADE


class Basemodel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    update_time = models.DateTimeField(auto_now=True, editable=False, null=True)
    created_by = models.ForeignKey(
        User, SET_NULL, null=True, blank=True, related_name="created_%(model_name)ss"
    )
    update_by = models.ForeignKey(
        User, SET_NULL, null=True, blank=True, related_name="updated_%(model_name)ss"
    )

    class Meta:
        abstract = True
        ordering = ("id",)


class Restaurant(Basemodel):
    name = models.CharField(max_length=225, null=True, blank=False)
    adress = models.CharField(max_length=225)
    photo = models.FileField(upload_to="media", null=True, blank=False)
    logo = models.FileField(upload_to="logo", null=True, blank=False)

    def __str__(self):
        return self.name


class Category(Basemodel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Menu(Basemodel):
    name = models.CharField(max_length=225, null=True, blank=False)
    description = models.CharField(max_length=225, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    photo = models.FileField()
    category = models.ForeignKey(Category, CASCADE, null=True, blank=True)
    discount = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
