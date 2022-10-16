from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries import Countries
from django_countries.fields import CountryField


class G8Countries(Countries):
    only = [
        'KR', 'CA', 'FR', 'DE', 'IT', 'JP', 'RU', 'GB',
        ('EU', _('European Union'))
    ]


# Create your models here.
class Company(models.Model):
    """
    회사
    """
    name = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=32,
        help_text='회사명'
    )
    email = models.EmailField(max_length=64, help_text='회사 이메일')
    country = CountryField(countries=G8Countries, blank_label='(국가를 선택해주세요.)')
    region = models.CharField(max_length=64, help_text='지역')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_cmpy_name_email'),
        ]


class Applicant(models.Model):
    """
    사용자(지원자)
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=32,
        help_text='지원자명'
    )
    email = models.EmailField(max_length=64, help_text='지원자 이메일')
    skill = models.CharField(max_length=32, help_text='사용 기술')
    objects = models.Manager()

    class Meta:
        db_table = 'applicant'
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_applicant_name_email'),
        ]


class JobPosting(models.Model):
    """
    채용 공고
    """
    company = models.ForeignKey(Company, related_name='job_postings', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, help_text='채용 제목')
    content = models.TextField()
    skill = models.CharField(max_length=32, help_text='사용 기술')
    recruit_compensation = models.IntegerField(help_text='채용 보상금')
    recruit_position = models.CharField(max_length=32, help_text='채용 포지션')

    objects = models.Manager()

    class Meta:
        db_table = 'job_posting'

    def __str__(self):
        return f'{self.company_id}: {self.title}'


class ApplicationHistory(models.Model):
    """
    지원 내역
    """
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        db_table = 'application_history'
        constraints = [
            models.UniqueConstraint(
                fields=['job_posting', 'applicant'],
                name='unique_applicant_history_job_posting_applicant'),
        ]
