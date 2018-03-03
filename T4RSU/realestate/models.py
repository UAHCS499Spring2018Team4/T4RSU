#!/usr/bin/env python3
# encoding=utf-8

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from .agency import Agency

# Create your models here.

class RealEstateAgentUserManager(BaseUserManager):
    def create_user(self, username: str, email, agency: 'Agency', password=None):
        """
        Create the user
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not isinstance(agency, Agency):
            agency = Agency.objects.get(pk=int(agency))
        if not agency:
            raise ValueError('Users must have an agency')
        if not isinstance(agency, Agency):
            raise ValueError('could not get agency')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            agency=agency,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, email, agency: 'Agency', password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            agency=agency
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class RealEstateAgentUser(AbstractBaseUser):
    """
    A real estate agent.
    """
    username = models.CharField(unique=True,
        max_length=1000) # ref: https://code.djangoproject.com/ticket/14094#comment:14
    USERNAME_FIELD = 'username'
    email = models.EmailField()
    EMAIL_FIELD = 'email'
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = ['email', 'agency']
    objects = RealEstateAgentUserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        # TODO: restrict ability to schedule showings
        # TODO: restrict ability to view sensitive information
        # TODO: restrict ability to provide feedback to creator
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
