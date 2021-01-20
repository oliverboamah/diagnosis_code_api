# Standart Library imports
import json

# Django imports
from django.test import (TestCase, Client)

# Third party imports
from rest_framework import status

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.code_types import (ICD_9, ICD_10)

# Test module for updating a diagnosis code record
class UpdateDiagnosisCodeApiTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.put_url = '/api/v1/codes/'

        self.first_record = DiagnosisCode.objects.create(
            id='Z20001', category_code='Z2000', diagnosis_code='1', 
            short_description='Short description of diagnosis', 
            full_description='This is a rather long description of the diagnosis',
            category_title='Cholera', code_type=ICD_10)

        self.second_record = DiagnosisCode.objects.create(
            id='Z20002', category_code='Z2000', diagnosis_code='2', 
            short_description='', 
            full_description='This is a rather long description of the diagnosis',
            category_title='', code_type=ICD_9)


        self.valid_payload = {
            "id": "Z20004", 
            "category_code": "Z2000", 
            "diagnosis_code": "4", 
            "short_description": "Short description of diagnosis", 
            "full_description": "This is a rather long description of the diagnosis",
            "category_title": "Cholera", 
            "code_type": "ICD_10"
        }

        self.invalid_payload = {
            "id": "", 
            "category_code": "Z2000", 
            "diagnosis_code": "5", 
            "short_description": "", 
            "full_description": "This is a rather long description of the diagnosis",
            "category_title": "", 
            "code_type": "ICD_09"
        }

    def test_valid_update_diagnosis_code_record(self):
        response = self.client.put(
            self.put_url + self.first_record.pk,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_diagnosis_code_record(self):
        response = self.client.put(
            self.put_url + self.second_record.pk,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
       