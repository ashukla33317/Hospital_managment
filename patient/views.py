
from django.shortcuts import redirect, render
from . import forms
from django.views import View
from .import models


class Patient(View):
    def get(self,request):
        content={
            'patient_form':forms.Patient_detail_form()
        }
        return render(request,"patient.html",content)


    def post(self,request):
        patient_name=request.POST['patient_name']
        patient_age=request.POST['patient_age']
        disease=request.POST['disease']
        ward_number=request.POST['ward_number']
        payment_detail=request.POST['payment_detail']
        phone_number=request.POST['phone_number']
        new_patient=models.Patient_detail(
            patient_name=patient_name,
            patient_age=patient_age,
            disease=disease,
            ward_number=ward_number,
            payment_detail=payment_detail,
            phone_number=phone_number

        )
        new_patient.save()
        return redirect('/')

class Details(View):
    def get(self,request):
        patient_id=request.GET['patient_id']
        content={
            'details':models.Patient_detail.objects.get(id=patient_id)
        }       
        return render(request,'details.html',content)

class Update_info(View):
    def get(self,request):
        patient_id = request.GET['patient_id']
        content = {
            'page_title':'Update details',
            'current_details':models.Patient_detail.objects.get(id = patient_id),
            'update_form':forms.Update_form()
        }
        return render(request,'new_patient.html',content)        

    
    def post(self,request):
        patient_name=request.POST['patient_name']
        patient_age=request.POST['patient_age']
        disease=request.POST['disease']
        ward_number=request.POST['ward_number']
        payment_detail=request.POST['payment_detail']
        phone_number=request.POST['phone_number']
        got_discharge = request.POST.get('got_discharge',False)
        print(got_discharge)


        current_info = models.Patient_detail.objects.get(id= patient_id)


        current_info.disease = current_info.disease if disease == '' else disease
        current_info.ward_number = current_info.ward_number if ward_number == '' else ward_number
        current_info.payment_detail = current_info.total_payment if payment_detail == '' else current_info.payment_detail+eval(payment_detail)
        current_info.phone_number  = current_info.phone_number if phone_number== '' else phone_number
        current_info.got_discharge = got_discharge
        current_info.save()

        return redirect('/')



