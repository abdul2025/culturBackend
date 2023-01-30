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
    pillarStanderQuestions = models.JSONField()
    pillar = models.ForeignKey(Phase, related_name='pillar', on_delete=models.CASCADE)



    def __str__(self):
        return self.name + str(self.id)


class Pillar(BaseModel):
    name = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)
    phase = models.ForeignKey(Phase, related_name='phases', on_delete=models.CASCADE)



    # def assignValuesToQuestions(self):
    #     pillarStanders = list(self.pallarStander.all())
    #     numberOfQuestions = 0
    #     ### Calculate questions weight
    #     for stander in pillarStanders:
    #         numberOfQuestions += len(stander.pillarStanderQuestions[0])
    #     questionWeight = round(self.weight / numberOfQuestions, 2)

    #     ### assign Question weight
    #     for stander in pillarStanders:
    #         for key, value in stander.pillarStanderQuestions[0].items():
    #             stander.pillarStanderQuestions[0][key] = questionWeight
    #         stander.save()





    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name + self.phase + f"weights: {self.weight}"

class Screening(BaseModel):
    name = models.CharField(max_length=255)
    questions = models.JSONField()
    tracks = models.ForeignKey(Tracks, related_name='tracks_screening', on_delete=models.CASCADE, null=False)



    def __str__(self):
        return self.name + str(self.id)


