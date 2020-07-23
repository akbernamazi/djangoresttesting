import datetime

from django.db.models import Q
from rest_framework import serializers
from .models import (KYC)


class KYCSerializer(serializers.ModelSerializer):

    class Meta:
        model = KYC
        fields = ('document_id', 'document', 'influencer_id',
                  'uploaded_date_time', 'status', 'reviewed_by', 'reviewed_date_time', 'document_type')

    def create(self, validated_data):
        data_inserted, created = KYC.objects.update_or_create(
            influencer_id=validated_data.get('influencer_id', None),
            document_type=validated_data.get('document_type'),
            defaults={
                'document': validated_data.get('document', None),
                'status': 'under_review',
                'uploaded_date_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        return data_inserted

    def destroy(self, validated_data):
        document_id = validated_data.get('document_id', None)
        influencer_id = validated_data.get('influencer_id', None)
        KYC.objects.filter(document_id=document_id,
                           influencer_id=influencer_id).delete()
