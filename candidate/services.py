
from .models import *
from typing import Iterable
from accounts.models import CustomUser
from .queries import *



### Used while a new
def calaculate_score_per_pillar(sub_app):
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


    #####TODO: Validate total given score are equal to the pillar weight
    sub_app.phase_score = phaseScore
    sub_app.save()

    return sub_app


class SubApplicationServices:

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
            else:
                return False
        ###
        # calc Phase subapp score
        # Calc pillar score
        calaculate_score_per_pillar(sub_app=sub_app)
        return sub_app


    @staticmethod
    def updateSubApplicationsQuestions(
            questions: list,
    ) -> CandidateSubApplication:
        sub_app: CandidateSubApplication
        for question in questions:
            stander = get_candidate_stander(id=question['id'])
            stander.stander_questions = question['stander_questions']
            stander.save()
            sub_app = stander.candidate_pillar.sub_application

        calaculate_score_per_pillar(sub_app=sub_app)
        return sub_app.application







