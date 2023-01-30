from accounts.models import *
from core.errors import Error, APIError

class CrmService:
    @staticmethod
    def getJudgeTracksbyUser(user):
        tracks = Judgers.objects.filter(user=user).values_list('tracks', flat=True)
        return list(tracks)
    @staticmethod
    def getfilteringTracksbyUser(user):
        tracks = Filtering.objects.filter(user=user).values_list('tracks', flat=True)
        print('fsakl')
        return list(tracks)
    @staticmethod
    def getsortTracksbyUser(user):
        tracks = Sorter.objects.filter(user=user).values_list('tracks', flat=True)
        return list(tracks)
    @staticmethod
    def getTrackInstances(ids):
        tracks = Tracks.objects.filter(pk__in=ids)
        return tracks
