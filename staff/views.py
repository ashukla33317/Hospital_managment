from django import forms
import patient
from patient.forms import Patient_detail_form
from django.shortcuts import redirect, render
from django.views import View
from patient.models import Patient_detail
from .import forms
# Create your views here.
class Home(View):
    def get(self,request):
        content={
            'patient_form':Patient_detail_form(),
            'patient_details':Patient_detail.objects.all()
        }
        return render(request,'index.html',content)

# class Delete_all(View):
#     def get(self,request):

#         patient_data=Patient_detail.objects.all()
#         patient_data.delete()
#         return redirect("/")
class Login_page(View):
    def get(self,request):
        content={
            'login_form':forms.Login_forms
        }
        return render(request,'login.html',content)

    def post(self,request):
        user_name=request.POST['user_name']  
        password=request.POST['password']
        print(user_name,password)
        return  redirect('/')

class Logout_page(View):
    def get(self,request):
        return redirect('/')   