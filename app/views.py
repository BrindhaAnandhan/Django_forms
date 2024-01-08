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

def Show(request):
    EFO1 = Show_Info_Forms()
    data = {'EFO1':EFO1, 'massage': ''}
    
    if request.method =="POST":
        SFDO = Show_Info_Forms(request.POST)
        try:
            if SFDO.is_valid():
                data['massage'] = "Yes you are our employee"
        except Exception as msg:
            data['massage'] = 'Error' + str(msg)

    return render(request, 'info.html', data)
        


