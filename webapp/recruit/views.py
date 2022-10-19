# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from recruit.models import Applicant, Company, JobPosting, ApplicationHistory
from recruit.serializers import ApplicantSerializer, CompanySerializer, \
    ApplicationHistorySerializer, JobPostingDetailSerializer, JobPostingListSerializer


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    지원자 view
    """
    queryset = Applicant.objects.all().order_by('name')
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.AllowAny]


class JobPostingViewSet(viewsets.ModelViewSet):
    """
    채용공고
    """
    queryset = JobPosting.objects.all().order_by('-id')
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['company__name', 'content',
                     'recruit_compensation', 'recruit_position', 'skill', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return JobPostingListSerializer
        return JobPostingDetailSerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    회사
    """
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]


class ApplicationHistoryViewSet(viewsets.ModelViewSet):
    """
    지원자
    """
    queryset = ApplicationHistory.objects.all().order_by('-id')
    serializer_class = ApplicationHistorySerializer
    permission_classes = [permissions.AllowAny]
