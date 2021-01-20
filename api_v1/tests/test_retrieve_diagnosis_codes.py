# Django imports
from django.test import (TestCase, Client)

# Third party imports
from rest_framework import status

# Local imports
from api_v1.models import DiagnosisCode
from api_v1.code_types import ICD_10

# Test module for retrieving diagnosis codes
class RetrieveDiagnosisCodesApiTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.get_url = '/api/v1/codes/'

        self.diagnosis_code_record = DiagnosisCode.objects.create(
            id='Z20001', category_code='Z2000', diagnosis_code='1', 
            short_description='Short description of diagnosis', 
            full_description='This is a rather long description of the diagnosis',
            category_title='Cholera', code_type=ICD_10)

    def test_retrieve_valid_diagnosis_code_record(self):

        response = self.client.get(self.get_url + self.diagnosis_code_record.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['category_code'], self.diagnosis_code_record.category_code)
        self.assertEqual(response.data['diagnosis_code'], self.diagnosis_code_record.diagnosis_code)
        self.assertEqual(response.data['short_description'], self.diagnosis_code_record.short_description)
        self.assertEqual(response.data['full_description'], self.diagnosis_code_record.full_description)
        self.assertEqual(response.data['category_title'], self.diagnosis_code_record.category_title)

    def test_retrieve_invalid_diagnosis_code_record(self):
        response = self.client.get(self.get_url + "200")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       