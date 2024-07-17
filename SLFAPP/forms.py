from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor
from django.contrib.auth.forms import AuthenticationForm


class PatientSignUpForm(UserCreationForm):
    profile_picture = forms.URLField(required=False)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', 'profile_picture', 'address')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            Patient.objects.create(user=user)
        return user


class DoctorSignUpForm(UserCreationForm):
    profile_picture = forms.URLField(required=False)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', 'profile_picture', 'address')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            Doctor.objects.create(user=user)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=150,
        help_text='Enter your username',
        error_messages={
            'required': 'Please enter your username',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter your password',
        error_messages={
            'required': 'Please enter your password',
        }
    )

    # Optional: You can uncomment and use clean method for login form validation
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if not user:
    #             raise forms.ValidationError(
    #                 'Invalid username or password. Please try again.')
    #     return cleaned_data
