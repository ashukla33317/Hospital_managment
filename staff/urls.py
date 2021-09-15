from django.urls import path
from . import views
from patient.views import Patient,Details,Update_info


urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('login',views.Login_page.as_view(),name="login"),
    path('logout',views.Logout_page.as_view(),name="logout"),
    path('add_patient',Patient.as_view(),name="patient"),
    path('details/',Details.as_view(),name="Details"),
    path('update/update',Update_info.as_view(),name='update_info'),
    path('update/',Update_info.as_view(),name='update_info')
    
]

# path('del_all',views.Delete_all.as_view(),name='delete_all')