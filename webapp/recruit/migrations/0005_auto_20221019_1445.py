# Generated by Django 3.2.14 on 2022-10-19 05:45

from django.db import migrations

from recruit.models import Company, Applicant


def init_company(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    company = apps.get_model("recruit", "Company")
    if not Company.objects.exists():
        db_alias = schema_editor.connection.alias
        company.objects.using(db_alias).bulk_create([
            Company(name="원티드랩",
                    email="biz@wantedlab.com",
                    country='KR',
                    region='서울특별시 송파구 올림픽로 300 롯데월드타워 35층'),
            Company(name="우아한 형제들",
                    email="help@woowahan.com",
                    country='KR',
                    region='서울시 송파구 위례성대로 2 (방이동, 장은빌딩)'),
        ])


def init_applicant(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    applicant = apps.get_model("recruit", "Applicant")
    if not Applicant.objects.exists():
        db_alias = schema_editor.connection.alias
        applicant.objects.using(db_alias).bulk_create([
            Applicant(name="이종성",
                    email="dlwhdtjd098@gmail.com",
                    skill='파이썬',),
            Applicant(name="삼종성",
                      email="tkawhdtjd098@gmail.com",
                      skill='자바',),
        ])


class Migration(migrations.Migration):
    dependencies = [
        ('recruit', '0004_remove_applicant_company'),
    ]

    operations = [
        migrations.RunPython(init_company),
        migrations.RunPython(init_applicant),
    ]