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
    class Meta:
        model = models.JobPosting
        read_only_fields = ('id',)
        fields = ['company', 'title', 'content', 'skill', 'recruit_compensation', 'recruit_position']


class ApplicationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = '__all__'
        model = models.ApplicationHistory
        fields = '__all__'
