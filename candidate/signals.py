# from django.dispatch import receiver
# from django.db.models import signals
# from .models import *
# from functools import wraps

# def prevent_recursion(func):

#     @wraps(func)
#     def no_recursion(sender, instance=None, **kwargs):

#         if not instance:
#             return

#         if hasattr(instance, '_dirty'):
#             return

#         func(sender, instance=instance, **kwargs)

#         try:
#             instance._dirty = True
#             instance.save()
#         finally:
#             del instance._dirty

#     return no_recursion


# @prevent_recursion
# @receiver(signals.post_save, sender=CandidateApplication)
# def update_scores(sender, instance, created, **kwargs):

#     instance.score = 6.0
#     instance.application_stage = 1
#     instance.save()