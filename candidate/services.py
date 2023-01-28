
from .models import *
from typing import Iterable
from accounts.models import CustomUser



### Used while a new
def calaculate_score_per_pillar(instance):
    queryset = instance.objects.filter(pillar=instance.pillar)
    ## Calculate Score by assigned pillar

    # retrive all sub app by pillar
        # answered 1 or 0
        # each answered * 10 to match weight formate
        # Sum all answered

    total_per_assigned_pillar = 0
    for pillars in list(queryset):
        for i in pillars.questions:

            # total_per_assigned_pillar += reduce(lambda x, y:int(x)+int(y), list(i.values())) * 10
            total_per_assigned_pillar += sum(list(map(int, i.values()))) * 10
    for subapp in list(queryset):
        CandidateSubApplication.objects.filter(id=subapp.id).update(score_per_pillar='total_per_assigned_pillar')


class NewSubApplicationServices:

    @staticmethod
    def CreateSubApplications(
            application: int,
            phase: str,
            pillars: list,
            reviewer: CustomUser
    ) -> CandidateSubApplication:
        sub_app, created = CandidateSubApplication.objects.get_or_create(
            application=application,
            phase_name=phase,
            reviewer=reviewer
            )
        for pillar in pillars:
            pillar_sub_app, created = CandidatePillarSubApplication.objects.get_or_create(
                sub_application=sub_app,
                pillar_name=pillar['name'],
                weight=pillar['weight'])
            if created:
                for stander in pillar['pillar_standers']:

                    stander = CandidateStanders(
                        candidate_pillar=pillar_sub_app,
                        stander_name=stander['name'],
                        stander_questions=stander['pillarStanderQuestions']
                    )
                    stander.save()


        ###
        # calc Phase subapp score
        # Calc pillar score


        subAppPillars = sub_app.candidates_sub_application.all()
        phaseScore = 0
        for pillar in subAppPillars:
            total_per_assigned_pillar = 0
            standers = pillar.candidates_pillar.all()
            for stander in standers:
                total_per_assigned_pillar += sum(list(map(int, stander.stander_questions.values())))
            pillar.score_per_pillar = total_per_assigned_pillar
            pillar.save()

            phaseScore += pillar.score_per_pillar
        sub_app.phase_score = phaseScore
        sub_app.save()

        return sub_app

