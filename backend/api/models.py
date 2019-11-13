from django.db import models
from rest_framework import serializers

from django.contrib.auth.models import User


class FitUser(User):
    name = models.CharField(max_length=250)
    age = models.IntegerField()  # age>18
    height = models.DecimalField(decimal_places=2, max_digits=3)
    weight = models.IntegerField()


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')
