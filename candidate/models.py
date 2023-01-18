from django.db import models
from accounts.models import BaseModel, CustomUser
from cultur.validators import _ID_NUMBER_REGEX
from django.core.validators import MaxValueValidator, MinValueValidator
import time
from core.utility import *
from datetime import timedelta, datetime

# Create your models here.
class CandidateProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    national_id = models.CharField(
        validators=[_ID_NUMBER_REGEX], max_length=10, blank=True, null=True
    )
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    is_saudi = models.BooleanField(default=True)
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'),
            ('F', 'Female')
        )
    )
    date_of_birth = models.DateField()
    age_range = models.CharField(max_length=255, null=True, blank=True)
    regdate = models.DateField()
    initiative_know = models.CharField(max_length=255, null=True, blank=True)

    status = models.IntegerField(
        choices=(
            (201, 'Approved'),
            (403, 'Blocked'),
        ),
        default=201
    )
    score = models.FloatField(null=True, blank=True, default=0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)

    cv = models.FileField(
        upload_to=PathAndRename(
            'uploads/cv/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )
    picture_id = models.FileField(
        upload_to=PathAndRename(
            'uploads/picture_id/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )


    def __str__(self):
        return self.user.name

    @property
    def descriptive_identification(self):
        return self.user.name

    # @property
    # def english_level(self):
    #     return self.english_level

    @property
    def get_photo_url(self):
         if self.picture_id and hasattr(self.picture_id, 'url'):
            return self.picture_id.url



    @property
    def age(self):
        if self.date_of_birth:
            month = (datetime.now().month - self.date_of_birth.month)
            year = datetime.now().year - self.date_of_birth.year
            if(month < 0):
                month = (datetime.now().month - self.date_of_birth.month) % 12
                year = datetime.now().year - self.date_of_birth.year - 1
                age = "{} Y | {} M".format(year, month)
            else:
                age = "{} Y | {} M".format(year, month)
            return age
        else:
            return '-'

    @property
    def show_age(self):
        year = datetime.now().year - self.date_of_birth.year
        return year

    # def does_contain_timeslot_with_munjiz(self, time_slot):
    #     status_query = Q(status=406) | Q(status=412)
    #     sessions = Session.objects.filter(
    #         Q(munjiz_id=self.id) & status_query & Q(time_slot=time_slot))

    #     if not sessions.exists():
    #         return False
    #     else:
    #         return True


    # def save(self, *args, **kwargs):
    #     self.score = (self.english_level_score + self.discipline + self.appearance + self.manner + self.experience) / 5
    #     return super().save(*args, **kwargs)

    # class Meta:
    #     verbose_name = 'Munjiz profile'
    #     verbose_name_plural = 'Munjiz profiles'