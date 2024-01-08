from django import forms
from app.models import *

class EmployeeForms(forms.Form):  
    Name = forms.CharField()
    Experience = forms.IntegerField()
    Mobile = forms.IntegerField()
    Email = forms.EmailField()
    Portfolio = forms.URLField()

class Show_Info_Forms(forms.Form):
    NO = [[Eo.Name, Eo.Name] for Eo in EmployeeInfo.objects.all()]
    Name = forms.ChoiceField(choices=NO)