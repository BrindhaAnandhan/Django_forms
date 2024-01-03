from django import forms

class EmployeeForms(forms.Form):
    
    Name = forms.CharField()
    Experience = forms.IntegerField()
    Mobile = forms.IntegerField()
    Email = forms.EmailField()
    Portfolio = forms.URLField()

