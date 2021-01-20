# Django imports
from django.db import models

# Local imports
from api_v1.code_types import ICD_10

# Create your models here.
class DiagnosisCode(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    category_code = models.CharField(null=True, max_length=100)
    diagnosis_code = models.CharField(null=True, max_length=100)
    short_description = models.TextField(null=True)
    full_description = models.TextField()
    category_title = models.CharField(null=True, max_length=255)
    code_type = models.CharField(default=ICD_10, max_length=10)
