from django.shortcuts import render
from app.views import *
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def Employee(request):
    EFO = EmployeeForms()
    data = {'EFO': EFO, 'message': ''}
    if request.method == 'POST':
        EFDO = EmployeeForms(request.POST)
        if EFDO.is_valid():
            name = EFDO.cleaned_data['Name']
            ex = EFDO.cleaned_data['Experience']
            mob =  EFDO.cleaned_data['Mobile']
            email = EFDO.cleaned_data['Email']
            pf = EFDO.cleaned_data['Portfolio']
            try:
                EOO = EmployeeInfo.objects.get_or_create(Name = name, Experience = ex, Mobile = mob, Email = email, Portfolio = pf)[0]
                EOO.save()
                data['message'] = "Employee is created successfully"
            except Exception as e:
                data['message'] = "Error: "+str(e)
        else:
            data['message'] = "Invalid"
    return render(request, 'Employee.html', data)