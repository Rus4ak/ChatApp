# Generated by Django 4.2.5 on 2023-09-19 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profiles/photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ImageField(default='profiles/profile-default-icon.png', upload_to='profiles/icons/%Y/%m/%d'),
        ),
    ]
