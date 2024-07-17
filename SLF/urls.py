# myproject/urls.py

from django.contrib import admin
from django.urls import path
from SLFAPP import views as users_views
from SLFAPP.views import login_view, patient_dashboard, doctor_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name='home'),
    path('patient/signup/', users_views.patient_signup, name='patient_signup'),
    path('doctor/signup/', users_views.doctor_signup, name='doctor_signup'),
    path('login/', login_view, name='login'),
    path('patient/dashboard/<str:username>/',
         patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/<str:username>/',
         doctor_dashboard, name='doctor_dashboard'),
    # Add other app URLs as needed
]
