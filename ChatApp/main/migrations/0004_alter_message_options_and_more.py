# Generated by Django 4.2.5 on 2023-10-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_is_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['id'], name='main_messag_id_0d21d9_idx'),
        ),
    ]
