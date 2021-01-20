# Django imports
from django.shortcuts import render

# Third Party imports
from rest_framework import generics

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.serializers import DiagnosisCodeSerializer

class ListDiagnosisCodesAPIView(generics.ListAPIView):
    queryset = DiagnosisCode.objects.all()
    serializer_class = DiagnosisCodeSerializer
