from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
import random




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    account_number = models.CharField(max_length=3600 ,unique=True, null=True, blank=True)
    bio = models.CharField(max_length=60, blank=True, null=True)
    adress = models.CharField(max_length=260)
    createat = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.user.username
    

    
    
    def save(self, *args, **kwargs):
        if not self.pk and self.account_number is None:
            self.account_number = generate_unique_account_number()
        super(Profile, self).save(*args, **kwargs)
    
def generate_unique_account_number():
    while True:
        number = random.randint(100000, 1000000000)
        if not Profile.objects.filter(account_number=number).exists():
            return number

    
@receiver(post_save ,sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    