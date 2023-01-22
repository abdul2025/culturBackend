from django.db import models
from accounts.models import BaseModel, CustomUser
from cultur.validators import _ID_NUMBER_REGEX
from django.core.validators import MaxValueValidator, MinValueValidator
import time
from core.utility import *
from datetime import timedelta, datetime
from crm.models import Tracks, Phase, Pillar, PallarStander
from .services import *


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


    #### This is for stage screening only
    status = models.IntegerField(
        choices=(
            (201, 'Approved'),
            (403, 'Blocked'),
        ),
        default=201
    )

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

    previous_work_upload = models.FileField(
        upload_to=PathAndRename(
            'uploads/participation_file/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )
    support = models.IntegerField(
        choices=(
            (0, 'Yes'),
            (1, 'No'),
        ),
        default=1
    )

    support_details = models.TextField(null=True, blank=True)
    previous_activities = models.IntegerField(
        choices=(
            (0, 'Yes'),
            (1, 'No'),
        ),
        default=1
    )
    previous_activities_yes = models.TextField(null=True, blank=True)
    snapchat_url = models.URLField(null=True, blank=True)
    instagram_media_url = models.URLField(null=True, blank=True)
    youtube_media_url = models.URLField(null=True, blank=True)
    linked_media_url = models.URLField(null=True, blank=True)
    twitter_media_url = models.URLField(null=True, blank=True)
    other_media_url = models.URLField(null=True, blank=True)
    inspiration_story = models.TextField(null=True, blank=True)
    additional_files = models.TextField(null=True, blank=True)

    honors_upload = models.FileField(
        upload_to=PathAndRename(
            'uploads/honors_upload_file/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )

    local_award = models.FileField(
        upload_to=PathAndRename(
            'uploads/local_award_file/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )

    international_awards = models.FileField(
        upload_to=PathAndRename(
            'uploads/nternational_awards_file/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )
    tv_host = models.CharField(null=True, blank=True, max_length=255)
    press_interviews = models.CharField(null=True, blank=True, max_length=255)
    training_courses = models.CharField(null=True, blank=True, max_length=255)
    academic_certifications = models.CharField(null=True, blank=True, max_length=255)
    volunteering = models.URLField(null=True, blank=True)
    book_permit = models.URLField(null=True, blank=True)
    ownership_agreement = models.TextField(null=True, blank=True)


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


class CandidateApplication(BaseModel):
    profile = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    participation_title = models.CharField(max_length=255)
    participation_file = models.FileField(
        upload_to=PathAndRename(
            'uploads/participation_file/{}'.format(time.strftime("%Y/%m/%d"))),
        max_length=2048,
        blank=True, null=True
    )
    work_overview =  models.CharField(max_length=255)
    year_of_execution = models.CharField(max_length=255)
    work_publishing = models.IntegerField(
        choices=(
            (0, 'Yes'),
            (1, 'No'),
        ),
        default=1
    )
    profitable_projects = models.IntegerField(
        choices=(
            (0, 'Yes'),
            (1, 'No'),
        ),
        default=1
    )
    profitable_projects = models.IntegerField(default=0)
    score = models.FloatField(null=True, blank=True, default=0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
    application_stage = models.IntegerField(
        choices=(
            (0, 'Filteration'),
            (1, 'Judgement'),
        ),
        default=1
    )


    def update_applications_score(self, *args, **kwargs):
        queryset = CandidateSubApplication.objects.values('reviewer__name').annotate(models.Sum('score_per_pillar'))
        ## group by reviewers
        ## total_phase sum score_per_pillar / by number of reviewers
        ## total_phase / by number of phases

        number_of_reviwers = queryset.count()
        total = 0
        for obj in list(queryset):
            total += obj['score_per_pillar__sum']

        total = total / number_of_reviwers
        print(total)




    def save(self, *args, **kwargs):
        self.update_applications_score()
        super().save(*args, **kwargs)
    #### Candidate Can only have one Applications per track
    class Meta:
        unique_together = (("track","profile"),)

    def __str__(self):
        return self.profile.user.name + '-' + str(self.id) + '- Track' + str(self.track.id)


class CandidateSubApplication(BaseModel):
    application = models.ForeignKey(CandidateApplication, on_delete=models.CASCADE, related_name='candidates_tracks')
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, null=True)
    pillar = models.ForeignKey(Pillar, on_delete=models.CASCADE, null=True)
    pillar_stander = models.ForeignKey(PallarStander, on_delete=models.CASCADE, null=True)
    questions = models.JSONField(default=list)
    score_per_pillar = models.FloatField(null=True, blank=True, default=0)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)

    def _calaculate_score(self, *args, **kwargs):
        # queryset = CandidateSubApplication.objects.values('pillar__').annotate(models.Sum('score_per_pillar'))
        ## Calculate Score by number of pillar and total wight

        total = 0
        for i in self.questions:
            total = sum(list(map(int, i.values())))
        return total




    def save(self, *args, **kwargs):
        self.score_per_pillar = self._calaculate_score()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.application.track.name + "-" + self.phase.name