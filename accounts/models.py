from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAuthDataModels(models.Model):
    username = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Users password list'
        verbose_name_plural = 'Users password lists'


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
