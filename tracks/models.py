from django.db import models
from accounts.models import BaseModel
# Create your models here.



class Tracks(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + str(self.id)

class Phase(BaseModel):
    name = models.CharField(max_length=255)
    tracks = models.ForeignKey(Tracks, related_name='tracks', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name + '-' + str(self.tracks.name)


class PallarStander(BaseModel):
    name = models.CharField(max_length=255)
    pillarStanderQuestions = models.JSONField(default=list)

    def __str__(self):
        return self.name + str(self.id)


class Pillar(BaseModel):
    name = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    pallarStander = models.ManyToManyField(PallarStander, related_name='list_of_pallarStander', blank=True)


    def __str__(self):
        return self.name + str(self.id) + f"weights: {self.weight}"

class Screening(BaseModel):
    name = models.CharField(max_length=255)
    questions = models.JSONField(default=list)
    tracks = models.ForeignKey(Tracks, related_name='tracks_screening', on_delete=models.CASCADE, null=False)



    def __str__(self):
        return self.name + str(self.id)


