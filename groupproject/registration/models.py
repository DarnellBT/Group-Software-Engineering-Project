"""Module contains UserProfile table"""
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Class contains database table attributes"""
    userId = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    is_user = models.BooleanField(default=1)
    is_game_keeper = models.BooleanField(default=0)
    is_admin = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username
    
    