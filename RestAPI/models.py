# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Actor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    login = models.CharField(max_length=150)
    avatar_url = models.CharField(max_length=150)


class Repo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150)


class Event(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE, null=True)
