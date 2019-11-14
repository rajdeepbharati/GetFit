from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    age = models.IntegerField(null=True)  # age >= 18
    height = models.DecimalField(
        decimal_places=2, max_digits=3, null=True)  # in meter
    weight = models.IntegerField(null=True)  # in kg
    sex = models.SmallIntegerField(null=True)  # 0:male, 1:female, 2:others
    bmi = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    health = models.CharField(max_length=11, null=True)


# CHOICES = [('-woman', '1500'), ('-man ~woman', '2000'),
#            ('~man +woman', '2500'), ('+man', '3000')]

CHOICES = [(1500, 1500), (2000, 2000), (2500, 2500), (3000, 3000)]


class Diet(models.Model):
    calories = models.IntegerField(choices=CHOICES)
    breakfast = models.CharField(max_length=500)
    lunch = models.CharField(max_length=500)
    snack = models.CharField(max_length=500)
    dinner = models.CharField(max_length=500)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.appuser.save()
