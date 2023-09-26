from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Profile, Post
import os

# Signal to remove the old icon when it changes
@receiver(pre_save, sender=Profile)
def delete_old_icon(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Profile.objects.get(pk=instance.pk)

            if old_instance.icon != instance.icon:
                old_instance.delete_icon()
        
        except Profile.DoesNotExist:
            pass


# Signal to delete img file when deleting a post
@receiver(pre_delete, sender=Post)
def delete_post_photo(sender, instance, **kwargs):
    if instance.id:
        try:
            post = Post.objects.get(id=instance.id)
            post_path = post.photo.path

            if os.path.isfile(post_path):
                os.remove(post_path)
        
        except Post.DoesNotExist:
            pass
