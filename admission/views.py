from django.shortcuts import render
from .models import Admission
from .form import AdmissionForm,SignUpform
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def home(r):
    return render(r,'front.html')

def register(r):
    form = AdmissionForm()
    if r.method == 'POST':
        form =AdmissionForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentlist/')
    return render(r,'register.html',{'form':form})
@login_required()
def studentlist(r):
    stud_list = Admission.objects.all()
    return render(r,'student_list.html',{'stud_list':stud_list})

def updatelist(r,id):

    if r.method == 'POST':
        stud_list = Admission.objects.get(pk=id)
        form = AdmissionForm(r.POST,instance=stud_list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentlist/')
    else:
        stud_list = Admission.objects.get(pk=id)
        form = AdmissionForm(instance=stud_list)

    return render(r,'updatelist.html',{'form':form})

def delete(r,id):
    if r.method == 'POST':
        stud_list = Admission.objects.get(id=id)
        stud_list.delete()
        return HttpResponseRedirect('studentlist/')

def signup(r):
    form=SignUpform()
    if r.method=='POST':
        form=SignUpform(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()

    return render(r,'signup.html',{'form':form})

def logout(r):

    return render(r,'logout.html')

def login(r):
    return render(r,'login.html')