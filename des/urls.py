from django.urls import path
from .views import KYCView
urlpatterns = [
    path('kyc-details', KYCView.as_view(), name='kyc'),
    # path("remove_kyc_details", KYCView.as_view(), name='kyc_delete')
]
