from .models import ideas
from .models import contactus
from .models import Reg
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class problem_form(ModelForm):
    class Meta:
        model = ideas
        fields = ['problem_id','idea']

class RegForm(ModelForm):
    class Meta:
        model = Reg
        fields = ['Team_name','M1_Name','M1_email','M1_Mobile_no','M1_gender','M2_Name','M2_email','M2_Mobile_no','M2_gender','M3_Name','M3_email','M3_Mobile_no','M3_gender','M4_Name','M4_email','M4_Mobile_no','M4_gender','M5_Name','M5_email','M5_Mobile_no','M5_gender','Mentor_Name','Mentor_email','Mentor_Mobile_no','Mentor_gender']

class contactus_form(ModelForm):
    class Meta:
        model = contactus
        fields = ['name','email','subject']
