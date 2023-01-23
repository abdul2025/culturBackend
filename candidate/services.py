
from .models import CandidateSubApplication



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