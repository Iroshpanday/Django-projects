from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def build_Profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.created(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):    
    instance.profile.save()   
    
    