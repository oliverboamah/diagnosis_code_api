# Django imports
from django.test import (TestCase, Client)

# Third party imports
from rest_framework import status

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.serializers import DiagnosisCodeSerializer
from api_v1.code_types import (ICD_9, ICD_10)

# Test module for listing diagnosis codes
class ListAllDiagnosisCodesApiTest(TestCase):

    def setUp(self):
        self.client = Client()

        DiagnosisCode.objects.create(
            id='Z20001', category_code='Z2000', diagnosis_code='1', 
            short_description='Short description of diagnosis', 
            full_description='This is a rather long description of the diagnosis',
            category_title='Cholera', code_type=ICD_10)

        DiagnosisCode.objects.create(
            id='Z20002', category_code='Z2000', diagnosis_code='2', 
            short_description='', 
            full_description='This is a rather long description of the diagnosis',
            category_title='', code_type=ICD_9)

    def test_list_diagnosis_code_records(self):

        # get API response
        response = self.client.get('/api/v1/codes/')

        # get data from db
        diagnosis_codes = DiagnosisCode.objects.all()
        serializer = DiagnosisCodeSerializer(diagnosis_codes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)
       