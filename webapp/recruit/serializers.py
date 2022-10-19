from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from . import models
from .models import Company


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Applicant
        fields = ['name', 'email', 'skill']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        read_only_fields = ('id',)
        fields = ['name', 'email', 'country', 'region', 'job_postings']
        validators = [
            UniqueTogetherValidator(
                queryset=Company.objects.all(),
                fields=['name', 'email']
            )
        ]


class JobPostingSerializer(serializers.ModelSerializer):
    company__name = serializers.ReadOnlyField(source='company.name')
    company__country = serializers.ReadOnlyField(source='company.country.name')
    company__region = serializers.ReadOnlyField(source='company.region')

    class Meta:
        model = models.JobPosting
        read_only_fields = ('id',)
        fields = [
            'id',
            'company', 'company__name',
            'company__country', 'company__region',
            'title', 'skill', 'recruit_compensation', 'recruit_position']

class JobPostingListSerializer(JobPostingSerializer):
    pass

class JobPostingDetailSerializer(JobPostingSerializer):
    job_postings = serializers.SerializerMethodField()

    class Meta(JobPostingSerializer.Meta):
        fields = JobPostingSerializer.Meta.fields + ['content', 'job_postings']

    @staticmethod
    def get_job_postings(obj):
        return [x.id for x in obj.company.job_postings.all()]


class ApplicationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = '__all__'
        model = models.ApplicationHistory
        fields = '__all__'
