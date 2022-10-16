# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets

from recruit.models import Applicant, Company, JobPosting, ApplicationHistory
from recruit.serializers import ApplicantSerializer, CompanySerializer, JobPostingSerializer, \
    ApplicationHistorySerializer


def index(request):
    pass


class ApplicantViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Applicant.objects.all().order_by('name')
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().order_by('-id')
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicationHistory.objects.all().order_by('-id')
    serializer_class = ApplicationHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
