import datetime
from django.shortcuts import render,redirect
from accounts.form import AppointmentForm

from accounts.models import Appointment, Doctor,User


# ---------------Home page  functions--------------

def home(request):
    doctors = Doctor.objects.all()

    data = {
        'doctors':doctors,
    }
    return render(request, 'pages/index.html',data)

# ---------------Appointment  functions--------------

def bookappointment(request):
    fm=AppointmentForm()
    if request.method == 'POST':
        fm =AppointmentForm(request.POST )
        if fm.is_valid():
            new= fm.save(commit=False)
            new.patient=request.user
            fm.save()
            return redirect('home')
        else:
            fm = AppointmentForm()
  
    return render(request, 'pages/bookappointment.html',{'fm':fm})


def appointmentdetail(request, id):
    appointment=Appointment.objects.get(id=id)
    form=AppointmentForm(instance=appointment)
    if request.method == 'POST':
        fm =AppointmentForm(request.POST ,instance=appointment)
        if fm.is_valid():
            fm.save()
            
            return redirect('home')
    data = {'form':form}
    return render(request, 'pages/appointdetail.html',data)

def appointmentdelete(request, id):
    appointment=Appointment.objects.get(id=id)
    
    if request.method == 'POST':
        appointment.delete()
        return redirect('/dashboard')
    data = {'appointment':appointment}
    return render(request, 'pages/appointdelete.html',data)

# ---------------dashboard functions--------------

def dashboardPatiend(request):

    object=Appointment.objects.filter(patient=request.user)

    data ={

        'object':object,
    }
    return render(request, 'pages/dashbord.html',data)

def dashboardDoctor(request):
    if request.method == 'POST':
        fdate = request.POST.get('fdate')
        tdate = request.POST.get('tdate')
        object =Appointment.objects.filter(doctor__id=request.user.doctor.id,date__gte=fdate,date__lte=tdate)
    else:
        object =Appointment.objects.filter(doctor__id=request.user.doctor.id)
    
    data = {
        
        'object': object,
        
    }

    return render(request, 'pages/dashboardDoctor.html',data)