from django.urls import path, include


from .views import *
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('screeing', views.ScreeningCndidateApplicationView,
                basename='screeing')

urlpatterns = [
    path('', ListProfilesView.as_view(), name='profiles'),
    path('<int:pk>/', RetriveProfilesView.as_view(), name='profile'),
    path('<int:truckid>/application/', ListCandidateApplicationsView.as_view(), name='applications'),
    path('application/<int:pk>', RetriveCandidateApplicationView.as_view(), name='application'),
    path('app/', NewCndidateApplicationView.as_view(), name='new_application'),
    # path('app/screeing', ScreeningCndidateApplicationView.as_view(), name='screening_application'),
    path('app/', include(router.urls)),

]