from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from cultur.validators import _PHONE_REGEX, _NAME_REGEX
from enum import Enum
from django.contrib.auth.base_user import BaseUserManager
from crm.models import Tracks
from core.utility import BaseModel


class GroupEnum(Enum):
    ADMIN_GROUP = 'Admin'
    JUDGEMENT_GROUP = 'Judgement'
    SORT_GROUP = 'Sort'
    FILTERING_GROUP = 'Filtering'
    REGULAR_GROUP = 'Regular'






class CustomUser(AbstractUser):
    ordering = ('username',)
    username = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(_('Mobile Number'), null=True, validators=[_PHONE_REGEX], max_length=10)
    is_blocked = models.BooleanField(default=False)

    class Meta:
        ordering = ('username', 'password')

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)


class Judgers(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="judgers")
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.user.email


class Filtering(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="filtering")
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.user.email

class Sorter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="sorters")
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.user.email






class LoginLog(BaseModel):
    email = models.EmailField(null=True)

    def __str__(self):
        return '{} Logged in at {}'.format(self.email, self.created_at)

