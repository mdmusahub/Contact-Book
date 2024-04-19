from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def contactinfo(request):
    return render(request,'index.html')

def addcontact(request):
    data = dict(request.GET)
    C_id = int(data['C_id'][0])
    C_name = data['C_name'][0]
    C_number = data['C_number'][0]
    C_email = data['C_email'][0]
    C_address = data['C_address'][0]


    data = models.ContactInfo(C_id,C_name,C_number,C_email,C_address)
    data.save()


    return redirect('/viewallcontact')

def updatecontact(request):
    data = dict(request.GET)
    uC_id = int(data['uC_id'][0])
    uC_name = data['uC_name'][0]
    uC_number = data['uC_number'][0]
    uC_email = data['uC_email'][0]
    uC_address = data['uC_address'][0]

    data = models.ContactInfo.objects.filter(C_id=uC_id).update(C_id=uC_id,C_name=uC_name,C_number=uC_number,C_email=uC_email,C_address=uC_address) 

    return redirect('/viewallcontact')

def deletecontact(request):
    data = dict(request.GET)

    uC_id = int(data['uC_id'][0])

    data = models.ContactInfo.objects.filter(C_id=uC_id).delete()

    return redirect('/viewallcontact')


def viewallcontact(request):
    data = list(models.ContactInfo.objects.all().values())

    return render(request,'viewallcontact.html',{'data':data})