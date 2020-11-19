from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['stu_name','stu_roll','stu_contact','stu_email','stu_faculty']
        widgets={
            'stu_name':forms.TextInput(attrs={'class':'form-control w-50'}),
            'stu_roll':forms.TextInput(attrs={'class':'form-control w-50'}),
            'stu_contact':forms.TextInput(attrs={'class':'form-control w-50'}),
            'stu_email':forms.EmailInput(attrs={'class':'form-control w-50'}),
            'stu_faculty':forms.TextInput(attrs={'class':'form-control w-50'})
        }

      
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class EditUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_active']

class EditAdminForm(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'