from django.urls import path, include


from .views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('applications', OpportunityApplicationViewSet, basename='applied-opportunities')




urlpatterns = [
    path('', ListProfilesView.as_view(), name='profiles'),
    path('<int:pk>/', RetriveProfilesView.as_view(), name='profile'),
    path('application/<int:pk>', CandidateApplicationView.as_view(), name='application'),

    # path('<int:pk>/phase/', ListPhasesView.as_view(), name='phase'),

]