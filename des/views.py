import logging

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import (FormParser,
                                    JSONParser,
                                    MultiPartParser,
                                    FileUploadParser,
                                    JSONParser)

from django.db import connection
from .models import (KYC)
from .serializers import (KYCSerializer)

# Create your views here.
LOGGER = logging.getLogger(__name__)


def save_kyc_details(data):

    serializer = KYCSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return {'error': serializer.errors}


def delete_kyc_details(data):
    serializer = KYCSerializer(data=data)
    if serializer.is_valid():
        serializer.destroy(data)
        return {}
    return {'error': serializer.errors}


def get_kyc_details(influencers_id):

    try:
        queryset = KYC.objects.filter(influencer_id=influencers_id)
        influencer_data = KYCSerializer(queryset, many=True)
        return influencer_data.data
    except Exception as exp:
        LOGGER.error(exp)
        return {}


class KYCView(APIView):

    parser_classes = (MultiPartParser, )

    def get(self, request):
        query_params = request.query_params
        influencer_id = query_params.get('influencer_id')

        return Response(get_kyc_details(influencer_id), status=status.HTTP_200_OK)

    def post(self, request):

        LOGGER.info("KYC REQUEST REACHED")
        data = request.data
        LOGGER.info(data)
        file = request.FILES['file']
        return Response(save_kyc_details({'document': file, 'influencer_id': data['influencer_id'],
                                          'document_type': data['document_type']}), status=status.HTTP_200_OK)
        # return Response({})

    def delete(self, request):
        query_params = request.query_params
        influencer_id = query_params.get('influencer_id')
        document_id = query_params.get('document_id')
        LOGGER.info("DOCUMENT DELETE REQUEST REACHED")
        # LOGGER.info(data)
        return Response(delete_kyc_details({'influencer_id': influencer_id, 'document_id': document_id}), status=status.HTTP_200_OK)
