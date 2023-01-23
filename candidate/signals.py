from django.dispatch import receiver
from django.db.models import signals
from .models import *
from functools import wraps
from .services import *


def prevent_recursion(func):

    @wraps(func)
    def no_recursion(sender, instance=None, **kwargs):

        if not instance:
            return

        if hasattr(instance, '_dirty'):
            return

        func(sender, instance=instance, **kwargs)

        try:
            instance._dirty = True
            instance.save()
        finally:
            del instance._dirty

    return no_recursion


# @prevent_recursion
# @receiver(signals.pre_save, sender=CandidateSubApplication)
# def on_change(sender, instance: CandidateSubApplication, **kwargs):
#     if crea
#         previous = CandidateSubApplication.objects.get(id=instance.id)
#         queryset = CandidateSubApplication.objects.filter(pillar=instance.pillar)
#     ## Calculate Score by assigned pillar

#     # retrive all sub app by pillar
#         # answered 1 or 0
#         # each answered * 10 to match weight formate
#         # Sum all answered

#         total_per_assigned_pillar = 0
#         for pillars in list(queryset):
#             for i in pillars.questions:
#                 # total_per_assigned_pillar += reduce(lambda x, y:int(x)+int(y), list(i.values())) * 10
#                 total_per_assigned_pillar += sum(list(map(int, i.values()))) * 10


#         if previous.score_per_pillar != total_per_assigned_pillar: # field will be updated
#             instance.score_per_pillar = total_per_assigned_pillar
#             instance.save()


# @receiver(signals.pre_save, sender=CandidateSubApplication)
# def on_change(sender, instance: CandidateSubApplication, **kwargs):
#     queryset = CandidateSubApplication.objects.filter(pillar=instance.pillar)
#     ## Calculate Score by assigned pillar

#     # retrive all sub app by pillar
#         # answered 1 or 0
#         # each answered * 10 to match weight formate
#         # Sum all answered

#     total_per_assigned_pillar = 0
#     for pillars in list(queryset):
#         for i in pillars.questions:

#             # total_per_assigned_pillar += reduce(lambda x, y:int(x)+int(y), list(i.values())) * 10
#             total_per_assigned_pillar += sum(list(map(int, i.values()))) * 10

#     for pillars in list(queryset):
#         pillars.score_per_pillar = total_per_assigned_pillar

#     instance.save()




# @prevent_recursion
# @receiver(signals.post_save, sender=CandidateApplication)
# def update_scores(sender, instance, created, **kwargs):
#     if created:
#         queryset = instance.objects.filter(pillar=instance.pillar)
#         ## Calculate Score by assigned pillar

#         # retrive all sub app by pillar
#             # answered 1 or 0
#             # each answered * 10 to match weight formate
#             # Sum all answered

#         total_per_assigned_pillar = 0
#         for pillars in list(queryset):
#             for i in pillars.questions:

#                 # total_per_assigned_pillar += reduce(lambda x, y:int(x)+int(y), list(i.values())) * 10
#                 total_per_assigned_pillar += sum(list(map(int, i.values()))) * 10
#         for subapp in list(queryset):
#             CandidateSubApplication.objects.filter(id=subapp.id).update(score_per_pillar='total_per_assigned_pillar')