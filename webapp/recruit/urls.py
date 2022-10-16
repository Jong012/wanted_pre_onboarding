from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('applicant', views.ApplicantViewSet)
router.register('job-posting', views.JobPostingViewSet)
router.register('company', views.CompanyViewSet)
router.register('application-history', views.ApplicationHistoryViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls), name='recruit')
]
