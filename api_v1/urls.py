# Django imports
from django.urls import path

# Local imports
from api_v1.views import ListDiagnosisCodesAPIView

urlpatterns = [
    path('codes', ListDiagnosisCodesAPIView.as_view()),
]
