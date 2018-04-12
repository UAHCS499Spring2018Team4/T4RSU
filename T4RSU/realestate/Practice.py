#!/usr/bin/env python3
# encoding=utf-8

from django.db import models


class Practice(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name
