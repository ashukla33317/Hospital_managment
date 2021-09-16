
from django.shortcuts import redirect, render
from . import forms
from django.views import View
from .import models
import patient


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
        return render(request,'update_info.html',content)        

    
    def post(self,request):
        patient_id = request.POST['patient_id']
        disease=request.POST['disease']
        ward_number=request.POST['ward_number']
        payment_detail=request.POST['payment_detail']
        discharge = request.POST.get('discharge',False)
        print(discharge)


        current_info = models.Patient_detail.objects.get(id= patient_id)


        current_info.disease = current_info.disease if disease == '' else disease
        current_info.ward_number = current_info.ward_number if ward_number == '' else ward_number
        current_info.payment_detail = current_info.payment_detail if payment_detail == '' else current_info.payment_detail+eval(payment_detail)
        current_info.discharge = discharge
        current_info.save()

        return redirect('/')



class Appointment(View):
    def get(self,request):
        content={
            'appointment_form':forms.Appointment_forms()
        }
        return render(request,'appointment.html',content)

    def post(self,request):
        patient_name=request.POST['patient_name']    
        patient_age=request.POST['patient_age']
        phone_number=request.POST['phone_number']
        appointment_date=request.POST['appointment_date']
        update_appointment=models.Appointment(
            patient_name=patient_name,
            patient_age=patient_age,
            phone_number=phone_number,
            appointment_date= appointment_date
            )
        update_appointment.save()
        return redirect('/')