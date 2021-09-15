from django import forms

class Patient_detail_form(forms.Form):
    patient_name=forms.CharField(max_length=20)
    patient_age=forms.IntegerField()
    disease=forms.CharField(max_length=50)
    ward_number=forms.IntegerField()
    payment_detail=forms.IntegerField()
    phone_number=forms.CharField(max_length=20)

class Update_form(forms.Form):
    patient_name=forms.CharField(required=False)
    patient_age=forms.IntegerField(required=False)
    disease=forms.CharField(required=False)
    ward_number=forms.IntegerField(required=False)
    payment_detail=forms.IntegerField(required=False)
    phone_number=forms.CharField(required=False)
    discharge = forms.BooleanField(required = False)