#!/usr/bin/env python3
# encoding=utf-8

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from .agency import Agency

class RealEstateAgentUserManager(BaseUserManager):
    def create_user(self, username: str, email: str, phone, agency: 'Agency', password: str=None, is_super: bool=False):
        """
        Create the user
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have a phone number')
        if not is_super:
            if not isinstance(agency, Agency):
                try:
                    int_agency = int(agency)
                except ValueError as e:
                    raise ValueError('Can\'t get pk for agency lookup') from e
                agency = Agency.objects.get(pk=int_agency)

                user = self.model(
                    username=username,
                    email=self.normalize_email(email),
                    phone=phone,
                    agency=agency,
                )
        else:
            user = self.model(
                username=username,
                email=self.normalize_email(email),
                phone=phone,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, email: str, phone, agency: 'Agency', password: str):
        """
        Creates and saves a superuser.
        """
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            username=username,
            agency=agency,
            is_super=True
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
    phone = models.CharField(max_length=1000, null=True)
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = ['email', 'agency', 'phone']
    objects = RealEstateAgentUserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None) -> bool:
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        # TODO: restrict ability to schedule showings
        # TODO: restrict ability to view sensitive information
        # TODO: restrict ability to provide feedback to creator
        return True

    def has_module_perms(self, app_label) -> bool:
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self) -> bool:
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
