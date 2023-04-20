from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))


    return render(request, 'Student.html', d)
