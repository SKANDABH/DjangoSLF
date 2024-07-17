
from .forms import LoginForm
from django.shortcuts import render, redirect
from .forms import PatientSignUpForm, DoctorSignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PatientSignUpForm, DoctorSignUpForm, LoginForm
from django.http import HttpResponse


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            # emailid = form.cleaned_data.get('email')
            # firstname = form.cleaned_data.get('first_name')
            # lastname = form.cleaned_data.get('last_name')
            # address = form.cleaned_data.get('address')
            #  , emailid=emailid,firstname=firstname,lastname=lastname,adres

            # Redirect to patient dashboard
            return redirect('patient_dashboard', username=username)
    else:
        form = PatientSignUpForm()
    return render(request, 'patient_signup.html', {'form': form})


def doctor_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Redirect to doctor dashboard
            return redirect('doctor_dashboard', username=username)
    else:
        form = DoctorSignUpForm()
    return render(request, 'doctor_signup.html', {'form': form})


# def login_view(request):
#     if request.user.is_authenticated:
#         if request.user.is_patient:
#             return redirect('patient_dashboard', username=request.user.username)
#         elif request.user.is_doctor:
#             return redirect('doctor_dashboard', username=request.user.username)
#         else:
#             # Redirect to login page if user's role is undefined
#             return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return HttpResponse("Please enter both username and password.", status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_patient:
                return redirect('patient_dashboard', username=username)
            elif user.is_doctor:
                return redirect('doctor_dashboard', username=username)
            else:
                return redirect('login')
        else:
            return HttpResponse("Invalid username or password.", status=401)
    else:
        # Handle GET request to render the login page
        return render(request, 'login.html')


def patient_dashboard(request, username):
    return render(request, 'patient_dashboard.html', {'username': username, 'user': request.user})


def doctor_dashboard(request, username):
    return render(request, 'doctor_dashboard.html', {'username': username, 'user': request.user})


def home(request):
    return render(request, 'home.html')
