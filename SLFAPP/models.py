# SLFAPP/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    profile_picture = models.URLField(blank=True)
    address = models.TextField()

    groups = models.ManyToManyField(
        Group,
        related_name='SLFAPP_user_set',  # Add this line
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='SLFAPP_user_set',  # Add this line
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='patient_profile')
    # Add any additional fields specific to patients


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor_profile')
    # Add any additional fields specific to doctors
