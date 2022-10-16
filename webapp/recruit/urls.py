from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('applicant',views.ApplicantViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls), name='applicant')
]
