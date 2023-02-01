from .models import *
from typing import Iterable
from core.errors import Error, APIError
from accounts.models import GroupEnum


# def get_tracks() -> Iterable[Tracks]:
#     try:
#         tracks = Tracks.objects.all()
#         return tracks
#     except Tracks.DoesNotExist:
#         raise APIError(Error.INSTANCE_NOT_FOUND, extra=[Tracks._meta.model_name])

def _fetchstatusStr(status):
    switcher = {
        GroupEnum.SORT_GROUP.value: 0,
        GroupEnum.FILTERING_GROUP.value: 1,
        GroupEnum.JUDGEMENT_GROUP.value: 2
    }
    return switcher.get(status, status)


def get_profile(id:int) -> CandidateProfile:
    try:
        return CandidateProfile.objects.get(id=id)
    except CandidateProfile.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[CandidateProfile._meta.model_name])


def get_applications(truckid:int, request) -> CandidateApplication:
    try:
        groups = request.user.groups.values_list('name',flat = True)
        groups = [_fetchstatusStr(i) for i in list(groups)]
        return CandidateApplication.objects.filter(track=truckid, application_stage__in=groups)
    except CandidateApplication.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[CandidateApplication._meta.model_name])


def get_application(id:int) -> CandidateApplication:
    try:
        return CandidateApplication.objects.get(id=id)
    except CandidateApplication.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[CandidateApplication._meta.model_name])

def get_candidate_screening_by_app(app:CandidateApplication) -> CandidateScreening:
    try:
        return CandidateScreening.objects.filter(application=app)
    except CandidateScreening.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[CandidateScreening._meta.model_name])


def get_candidate_stander(id:int) -> CandidateStanders:
    try:
        return CandidateStanders.objects.get(id=id)
    except CandidateStanders.DoesNotExist:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[CandidateStanders._meta.model_name])




# def get_phase_by_track(id:int) -> Iterable[Phase]:
#     try:
#         return Phase.objects.filter(tracks=id)
#     except Phase.DoesNotExist:
#         raise APIError(Error.INSTANCE_NOT_FOUND, extra=[Phase._meta.model_name])

# def get_phase(id:int) -> Tracks:
#     try:
#         return Phase.objects.get(id=id)
#     except Phase.DoesNotExist:
#         raise APIError(Error.INSTANCE_NOT_FOUND, extra=[Phase._meta.model_name])

# def get_pillar_by_phase(phase:Phase) -> Iterable[Phase]:
#     try:
#         return Pillar.objects.filter(phase=phase)
#     except Pillar.DoesNotExist:
#         raise APIError(Error.INSTANCE_NOT_FOUND, extra=[Pillar._meta.model_name])

# def get_screening_by_track(track:Tracks) -> Iterable[Phase]:
#     try:
#         return Screening.objects.filter(tracks=track)
#     except Screening.DoesNotExist:
#         raise APIError(Error.INSTANCE_NOT_FOUND, extra=[Screening._meta.model_name])