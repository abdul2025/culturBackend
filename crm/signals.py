from django.dispatch import receiver
from django.db.models import signals
from .models import *
from functools import wraps


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

@prevent_recursion
@receiver(signals.m2m_changed, sender=Pillar.pallarStander.through)
def changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    pk_set = kwargs.pop('pk_set', None)
    action = kwargs.pop('action', None)
    # or action == "pre_remove"

    list_keys = list(instance.pallarStander.all().values_list('id', flat=True))
    list_standers = []
    if action == "pre_add":
        for key in list(pk_set):
            if key not in list_keys:
                print(key)
                stander = PallarStander.objects.get(pk=key)
                list_standers.append(stander)


        pillarStanders = list(instance.pallarStander.all())
        pillarStanders = pillarStanders + list_standers
        numberOfQuestions = 0
        ### Calculate questions weight
        for stander in pillarStanders:
            numberOfQuestions += len(stander.pillarStanderQuestions)


        ### If list of question is empty in pillar standers
        if numberOfQuestions >= 1:
            questionWeight = round(instance.weight / numberOfQuestions, 2)

            ### assign Question weight
            for stander in pillarStanders:
                for key, value in stander.pillarStanderQuestions.items():
                    stander.pillarStanderQuestions[key] = questionWeight
                stander.save()
    if action == "pre_remove":
        print('Stander is removed')
        #### Should never Happen

                # instance.pallarStander.add(stander)
                # instance.save()
                # print(count)
                # print(instance.pallarStander.count())


        #     if count != instance.pallarStander.count():
        #         # pillar = Pillar.objects.get(pallarStander=instance)

        #         pillarStanders = list(instance.pallarStander.all())
        #         print(pillarStanders)
                # numberOfQuestions = 0
                # ### Calculate questions weight
                # for stander in pillarStanders:
                #     numberOfQuestions += len(stander.pillarStanderQuestions[0])
                # questionWeight = round(pillar.weight / numberOfQuestions, 2)

                # ### assign Question weight
                # for stander in pillarStanders:
                #     for key, value in stander.pillarStanderQuestions[0].items():
                #         stander.pillarStanderQuestions[0][key] = questionWeight
                #     stander.save()


            # print(instance.pallarStander.count())
            # print(count)


            # c = Category.objects.get(pk=1)
            # instance.category.add(c)
            # instance.save()




# @prevent_recursion
# @receiver(signals.post_save, sender=Pillar)
# def update_scores(sender, instance, created, **kwargs):
#         pre = Pillar.objects.get(id=instance.id)
#         count = pre.pallarStander.count()
#         print(instance.pallarStander.count())
#         print(count)
        # if count != instance.pallarStander.count():
        #     print('k')
        # pillar = Pillar.objects.get(pallarStander=instance)

        # pillarStanders = list(pillar.pallarStander.all())
        # numberOfQuestions = 0
        # ### Calculate questions weight
        # for stander in pillarStanders:
        #     numberOfQuestions += len(stander.pillarStanderQuestions[0])
        # questionWeight = round(pillar.weight / numberOfQuestions, 2)

        # ### assign Question weight
        # for stander in pillarStanders:
        #     for key, value in stander.pillarStanderQuestions[0].items():
        #         stander.pillarStanderQuestions[0][key] = questionWeight
        #     stander.save()