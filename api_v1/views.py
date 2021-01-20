# Django imports
from django.shortcuts import render

# Third Party imports
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.serializers import DiagnosisCodeSerializer

class ListCreateDiagnosisCodesAPIView(ListCreateAPIView):
    queryset = DiagnosisCode.objects.all()
    serializer_class = DiagnosisCodeSerializer

class RetrieveUpdateDestroyDiagnosisCodeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DiagnosisCode.objects.all()
    serializer_class = DiagnosisCodeSerializer