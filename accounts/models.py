from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from cultur.validators import _PHONE_REGEX, _NAME_REGEX
from enum import Enum


class GroupEnum(Enum):
    ADMIN_GROUP = 'Admin'
    REGULAR_GROUP = 'Rugular'
    CANDIDATE_GROUP = 'Candidate'


class CustomUser(AbstractUser):
    ordering = ('username',)

    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    last_name = models.CharField(
        max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    phone_number = models.CharField(_('Mobile Number'), null=True, validators=[_PHONE_REGEX], max_length=10)
    is_blocked = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)


    class Meta:
        ordering = ('username', 'email', 'password')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True

class LoginLog(BaseModel):
    username = models.CharField(max_length=11)

    def __str__(self):
        return '{} Logged in at {}'.format(self.username, self.created_at)

