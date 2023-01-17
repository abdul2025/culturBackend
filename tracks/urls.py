from django.urls import path, include


from .views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('applications', OpportunityApplicationViewSet, basename='applied-opportunities')




urlpatterns = [
    path('', ListTracksView.as_view(), name='trackes'),

    path('<int:pk>/phase/', ListPhasesView.as_view(), name='phase'),
    path('phase/<int:pk>/pillar/', ListPillarView.as_view(), name='pillar'),
    path('<int:pk>/screening/', ListScreeningView.as_view(), name='screening'),
]