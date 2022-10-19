from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Applicant)
class AdminApplicant(admin.ModelAdmin):
    pass


@admin.register(models.JobPosting)
class AdminJobPosting(admin.ModelAdmin):
    pass


@admin.register(models.Company)
class AdminCompany(admin.ModelAdmin):
    pass


@admin.register(models.ApplicationHistory)
class ApplicationHistory(admin.ModelAdmin):
    pass
