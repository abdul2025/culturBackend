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




class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    ordering = ('email',)

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(_('Mobile Number'), null=True, validators=[_PHONE_REGEX], max_length=10)
    is_blocked = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('email', 'password')

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

