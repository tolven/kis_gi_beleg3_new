import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from kis_pro.forms import NewUserForms, NewPatientForms, NewDocForms, NewCaseForms, NewTNMForms, NewSurgeryForms
from kis_pro.models import User, Patient, Doctor, Cases, TNM, SurgeryData


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
    cases = Cases.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'cases': cases
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
            userid = x.pk
            return redirect('kis_pro_detail', pk=userid)
    else:
        form = NewPatientForms()
        return render(request, 'registration/kis_pro_newpatient.html', {'form': form})


def kis_pro_new_tnm(request, pk):
    if request.method == 'POST':
        case = Cases.objects.get(pk=pk)
        form = NewTNMForms(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.case = case
            x.save()
            return redirect('kis_pro_pathology', case.doctor.pk)
    else:
        form = NewTNMForms()
        return render(request, 'pathology/kis_pro_new_tnm.html', {'form': form})


def kis_pro_new_surgery(request, pk):
    if request.method == 'POST':
        case = Cases.objects.get(pk=pk)
        form = NewSurgeryForms(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.case = case
            x.save()
            return redirect('kis_pro_surgery', case.doctor.pk)
    else:
        form = NewSurgeryForms()
        return render(request, 'surgery/kis_pro_new_surgery.html', {'form': form})


def kis_pro_deleteuser(request, pk):
    doc = Doctor.objects.get(pk=pk)
    doc.delete()
    return redirect('kis_pro_index')


def kis_pro_deletepatient(request, pk):
    doc = Patient.objects.get(pk=pk)
    doc.delete()
    return redirect('kis_pro_registration')


def kis_pro_deleteregistration(request, pk):
    doc = User.objects.get(pk=pk)
    doc.delete()
    return redirect('kis_pro_index')


def kis_pro_registration(request):
    patient = Patient.objects.all()
    context = {
        'kis_patient': patient
    }
    return render(request, 'registration/kis_pro_registration.html', context)


def kis_pro_pathology(request, pk):
    doc = Doctor.objects.get(pk=pk)
    cases = Cases.objects.filter(doctor=doc)
    context = {
        'cases': cases
    }
    return render(request, 'pathology/kis_pro_pathology.html', context)


def kis_pro_pathology_meet(request, pk, caseid):
    try:
        tnm = TNM.objects.get(case_id=caseid)
        context = {
            'tnm': tnm
        }
        return render(request, 'pathology/kis_pro_pathology_meet.html', context)
    except ObjectDoesNotExist:
        cases = Cases.objects.get(pk=caseid)
        context = {
            'cases': cases
        }
        return render(request, 'pathology/kis_pro_pathology_meet.html', context)


def kis_pro_radiology(request, pk):
    doc = Doctor.objects.get(pk=pk)
    cases = Cases.objects.filter(doctor=doc)
    context = {
        'cases': cases
    }
    return render(request, 'radiology/kis_pro_radiology.html', context)


def kis_pro_surgery(request, pk):
    doc = Doctor.objects.get(pk=pk)
    cases = Cases.objects.filter(doctor=doc)
    context = {
        'cases': cases
    }
    return render(request, 'surgery/kis_pro_surgery.html', context)


def kis_pro_surgery_meet(request, pk, caseid):
    try:
        surgery = SurgeryData.objects.get(case_id=caseid)
        context = {
            'surgery': surgery
        }
        return render(request, 'surgery/kis_pro_surgery_meet.html', context)
    except ObjectDoesNotExist:
        cases = Cases.objects.get(pk=caseid)
        context = {
            'cases': cases
        }
        return render(request, 'surgery/kis_pro_surgery_meet.html', context)


def kis_pro_newcase(request, pk):
    if request.method == 'POST':
        form = NewCaseForms(request.POST)
        patient = Patient.objects.get(pk=pk)
        if form.is_valid():
            x = form.save(commit=False)
            x.patient = patient
            x.save()
            return redirect('kis_pro_registration')
    else:
        form = NewCaseForms()
        patient = Patient.objects.get(pk=pk)
        context = {
            'patient': patient,
            'form': form
        }
        return render(request, 'registration/kis_pro_newcase.html', context)
