from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mvt.models import kayit_kullaniciyi_gruba_ata


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=User)
def kullanici_kaydedildiginde(sender, instance, created, **kwargs):
    if created:
        kayit_kullaniciyi_gruba_ata(sender, instance, created, **kwargs)
