import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from kis_pro.forms import NewUserForms, NewPatientForms, NewDocForms
from kis_pro.models import User, Patient, Doctor


def kis_pro_index(request):
    user = User.objects.all()
    doc = Doctor.objects.all()
    context = {
        'user': user,
        'docs': doc
    }
    return render(request, 'kis_pro_index.html', context)


def kis_pro_detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {
        'patient': patient
    }
    return render(request, 'kis_pro_detail.html', context)


def kis_pro_newuser(request):
    if request.method == 'POST':
        request_val = request.POST
        x = request_val.get('role')
        if x == '1':
            form = NewUserForms(request.POST)
        else:
            form = NewDocForms(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('kis_pro_index')
    else:
        form = NewUserForms()
        return render(request, 'kis_pro_newuser.html', {'form': form})


def kis_pro_newpatient(request):
    if request.method == 'POST':
        form = NewPatientForms(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            return redirect('kis_pro_index')
    else:
        form = NewPatientForms()
        return render(request, 'kis_pro_newpatient.html', {'form': form})


def kis_pro_deleteuser(request, pk):
    doc = Doctor.objects.get(pk=pk)
    doc.delete()
    return redirect('kis_pro_index')


def kis_pro_registration(request):
    patient = Patient.objects.all()
    context = {
        'kis_patient': patient
    }
    return render(request, 'kis_pro_registration.html', context)


def kis_pro_pathology(request):
    patient = Patient.objects.all()
    context = {
        'kis_patient': patient
    }
    return render(request, 'kis_pro_pathology.html', context)


def kis_pro_radiology(request):
    patient = Patient.objects.all()
    context = {
        'kis_patient': patient
    }
    return render(request, 'kis_pro_radiology.html', context)


def kis_pro_surgery(request):
    patient = Patient.objects.all()
    context = {
        'kis_patient': patient
    }
    return render(request, 'kis_pro_surgery.html', context)
