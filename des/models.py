from django.db import models
from django_mysql.models import JSONField

# Create your models here.


class KYC(models.Model):

    document_id = models.AutoField(primary_key=True)
    document = models.FileField(upload_to='./influencer/kyc_documents',
                                null=True, default=None)
    influencer_id = models.IntegerField(default=0)
    uploaded_date_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50, blank=True, default='under_review')
    reviewed_by = models.CharField(max_length=25, null=True, default=None)
    reviewed_date_time = models.DateTimeField(null=True, default=None)
    document_type = models.CharField(max_length=25, null=True, default=None)
    rejection_reason = JSONField(max_length=2000, null=True, default=list)
