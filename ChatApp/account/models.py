from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='profiles/icons/%Y/%m/%d', default='profiles/profile-default-icon.png')

    def __str__(self):
        return f'Profile of {self.user.username}'
    

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/posts/%Y/%m/%d')
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.description
