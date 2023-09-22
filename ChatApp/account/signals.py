from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Profile

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
