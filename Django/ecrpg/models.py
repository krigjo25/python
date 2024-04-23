from datetime import datetime
from django.db import models

# Create your models here.


class ManagementTeam(models.Model):

    playerName = models.CharField(max_length=255)
    lvl = models.IntegerField()
    boss = models.CharField(max_length=255)

class BannedPlayer(models.Model):

    playerName = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255)
    adminName = models.CharField(max_length=255)

class WikiCategory(models.Model):

    name = models.CharField(max_length=20)
    img = models.FilePathField(path='/svg', blank=True)

class WikiPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ManyToManyField('WikiCategory', related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
