# Third Party imports
from rest_framework import serializers

# Local imports
from api_v1.models import DiagnosisCode

class DiagnosisCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisCode
        fields = ('id', 'category_code', 'diagnosis_code', 'short_description', 
        'full_description', 'category_title', 'code_type')