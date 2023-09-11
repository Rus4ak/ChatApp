from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='profiles/%Y/%m/%d', default='profiles/profile-default-icon.png')

    def __str__(self):
        return f'Profile of {self.user.username}'
