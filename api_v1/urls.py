# Django imports
from django.urls import path

# Local imports
from api_v1.views import (ListCreateDiagnosisCodesAPIView, RetrieveUpdateDestroyDiagnosisCodeAPIView)

urlpatterns = [
    path('', ListCreateDiagnosisCodesAPIView.as_view()),
    path('<str:pk>', RetrieveUpdateDestroyDiagnosisCodeAPIView.as_view()),
]