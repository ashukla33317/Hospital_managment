from django.db import models

# Create your models here.
class Patient_detail(models.Model):
    patient_name=models.CharField(max_length=20)
    patient_age=models.IntegerField()
    disease=models.CharField(max_length=50)
    ward_number=models.IntegerField()
    payment_detail=models.IntegerField()
    phone_number=models.CharField(max_length=20)