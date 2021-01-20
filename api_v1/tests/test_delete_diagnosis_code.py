# Standart Library imports
import json

# Django imports
from django.test import TestCase, Client

# Third party imports
from rest_framework import status

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.code_types import (ICD_9, ICD_10)

# Test module for deleting a diagnosis code record
class DeleteDiagnosisCodeApiTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.delete_url = '/api/v1/codes/'

        self.diagnosis_code_record = DiagnosisCode.objects.create(
            id='Z20001', category_code='Z2000', diagnosis_code='1', 
            short_description='Short description of diagnosis', 
            full_description='This is a rather long description of the diagnosis',
            category_title='Cholera', code_type=ICD_10)

    def test_valid_delete_diagnosis_code_record(self):
        response = self.client.delete(
            self.delete_url + self.diagnosis_code_record.pk
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_diagnosis_code_record(self):
        response = self.client.delete(
            self.delete_url + "100"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       