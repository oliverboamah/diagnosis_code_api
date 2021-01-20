# Standart Library imports
import json

# Django imports
from django.test import TestCase, Client

# Third party imports
from rest_framework import status

# Test module for creating a new diagnosis code record
class CreateDiagnosisCodeApiTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.post_url = '/api/v1/codes/'

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

    def test_create_valid_diagnosis_code_record(self):
        response = self.client.post(
            self.post_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_diagnosis_code_record(self):
        response = self.client.post(
            self.post_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
       