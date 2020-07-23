# Generated by Django 3.0.8 on 2020-07-18 08:22

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.FileField(default=None, null=True, upload_to='influencer/kyc_documents')),
                ('influencer_id', models.IntegerField(default=0)),
                ('uploaded_date_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, default='under_review', max_length=50)),
                ('reviewed_by', models.CharField(default=None, max_length=25, null=True)),
                ('reviewed_date_time', models.DateTimeField(default=None, null=True)),
                ('document_type', models.CharField(default=None, max_length=25, null=True)),
                ('rejection_reason', django_mysql.models.JSONField(default=list, max_length=2000, null=True)),
            ],
        ),
    ]
